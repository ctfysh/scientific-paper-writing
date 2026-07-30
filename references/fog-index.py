#!/usr/bin/env python3
"""
Gunning Fog Index Calculator for Scientific Writing.

Usage:
    python3 fog-index.py "<text>"
    python3 fog-index.py --file paragraph.txt
    python3 fog-index.py --interactive

Based on: Alley, The Craft of Scientific Writing, 4th Ed.
Formula: Fog = 0.4 × (ASL + PHW)
    ASL = Average Sentence Length (words / sentences)
    PHW = Percentage of Hard Words (complex words / words) × 100
    Complex = 3+ syllables, excluding proper nouns, compounds, -es/-ed suffixes
"""

import re
import sys
import argparse

# Common scientific suffixes that don't increase complexity
SUFFIXES = {
    "es", "ed", "ing",  # verb inflections
    "al", "ic", "ical",  # adjective suffixes (often 3+ syllable words are already complex with or without these)
}

# Known proper nouns and technical terms to exclude
# Users can extend this list for their domain
KNOWN_EXCEPTIONS = {
    "analysis", "synthesis", "polymer", "catalyst", "diameter",
    "parameter", "variable", "algorithm", "frequency", "particle",
    "molecule", "spectrum", "phenomenon", "hypothesis", "mitochondria",
}


def count_syllables(word: str) -> int:
    """Count syllables using a simple vowel-group heuristic."""
    word = word.lower().strip(".,!?;:()[]{}'\"")
    if not word:
        return 0
    # Count vowel groups
    vowels = "aeiouy"
    count = 0
    prev_vowel = False
    for char in word:
        is_vowel = char in vowels
        if is_vowel and not prev_vowel:
            count += 1
        prev_vowel = is_vowel
    # Ensure at least 1 syllable
    return max(1, count)


def is_complex(word: str) -> bool:
    """
    Determine if a word is 'complex' (3+ syllables).
    Excludes proper nouns, compound words, and common scientific terms.
    """
    word_clean = word.strip(".,!?;:()[]{}'\"")
    if not word_clean:
        return False

    # Check known exceptions
    if word_clean.lower() in KNOWN_EXCEPTIONS:
        return False

    # Check if capitalized (likely proper noun)
    if word_clean[0].isupper() and not word_clean.isupper():
        return False  # proper noun

    # Count syllables
    syl = count_syllables(word_clean)

    # Strip common suffixes and re-check
    for suffix in SUFFIXES:
        if word_clean.lower().endswith(suffix) and len(word_clean) > len(suffix) + 2:
            stripped = word_clean[: -len(suffix)]
            base_syl = count_syllables(stripped)
            if base_syl < 3:
                return False  # word was only complex due to suffix

    return syl >= 3


def gunning_fog(text: str) -> dict:
    """
    Calculate Gunning Fog Index and return detailed breakdown.
    """
    # Split into sentences
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if len(s.strip()) > 5]

    if not sentences:
        return {"error": "No sentences found", "fog": 0}

    # Extract words
    words = re.findall(r'\b[a-zA-Z]+\b', text)
    if not words:
        return {"error": "No words found", "fog": 0}

    word_count = len(words)
    sentence_count = len(sentences)

    # Identify complex words
    complex_words = [w for w in words if is_complex(w)]
    complex_count = len(complex_words)

    # Calculate
    asl = word_count / sentence_count
    phw = (complex_count / word_count) * 100
    fog = 0.4 * (asl + phw)

    return {
        "fog_index": round(fog, 1),
        "words": word_count,
        "sentences": sentence_count,
        "asl": round(asl, 1),
        "complex_words": complex_count,
        "phw": round(phw, 1),
        "complex_word_list": complex_words[:20],  # first 20 for inspection
        "verdict": _verdict(fog),
    }


def _verdict(fog: float) -> str:
    """Interpret Fog Index for scientific writing."""
    if fog < 10:
        return "TOO SIMPLE — May be oversimplified for scientific writing (target: 12-15)"
    elif 10 <= fog < 12:
        return "ADEQUATE — Accessible but may lose nuance"
    elif 12 <= fog <= 15:
        return "GOOD — On target for scientific writing"
    elif 15 < fog <= 17:
        return "DENSE — Consider simplifying sentences or vocabulary"
    elif 17 < fog <= 20:
        return "TOO DENSE — Paragraph needs restructuring"
    else:
        return "VERY DENSE — Likely to frustrate readers"


def main():
    parser = argparse.ArgumentParser(
        description="Gunning Fog Index Calculator for Scientific Writing"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("text", nargs="?", help="Text to analyze")
    group.add_argument("--file", "-f", help="Read text from file")
    group.add_argument("--interactive", "-i", action="store_true",
                       help="Interactive mode: type/paste paragraphs")

    args = parser.parse_args()

    if args.interactive:
        print("Gunning Fog Index Calculator (interactive mode)")
        print("Type or paste a paragraph. Empty line to exit.")
        print("-" * 50)
        while True:
            print("\nEnter paragraph:")
            lines = []
            while True:
                try:
                    line = input()
                    if not line:
                        break
                    lines.append(line)
                except EOFError:
                    break
            if not lines:
                break
            text = " ".join(lines)
            result = gunning_fog(text)
            if "error" in result:
                print(f"Error: {result['error']}")
            else:
                print_result(result)
        return

    if args.file:
        with open(args.file, "r") as f:
            text = f.read()
    else:
        text = args.text

    result = gunning_fog(text)
    if "error" in result:
        print(f"Error: {result['error']}")
    else:
        print_result(result)


def print_result(result: dict):
    print("-" * 50)
    print(f"Gunning Fog Index: {result['fog_index']}")
    print(f"  Words: {result['words']}")
    print(f"  Sentences: {result['sentences']}")
    print(f"  Avg Sentence Length: {result['asl']}")
    print(f"  Complex Words: {result['complex_words']} ({result['phw']}%)")
    print(f"  Verdict: {result['verdict']}")
    if result.get("complex_word_list"):
        complex_str = ", ".join(result["complex_word_list"])
        print(f"  Sample complex words: {complex_str}")
    print("-" * 50)


if __name__ == "__main__":
    main()
