# Scientific Paper Writing — Agent Skill

A structured agent skill for writing and revising scientific papers, based on two source books:

- **The Craft of Scientific Writing** (Michael Alley, 4th ed.)
- **Scientific Writing 3.0: A Reader and Writer's Guide** (Jean-Luc Lebrun & Justin Lebrun)

## What This Skill Does

Guides an AI agent through the full lifecycle of a scientific paper — from blank page to pre-submission draft — by applying Alley's craft principles (energy, flow, precision) and Lebrun's reader-aware strategy (knowledge gap, halo effect, confirmation bias).

## Structure

```
scientific-paper-writing/
├── SKILL.md              ← Main entry point (read this first)
├── README.md             ← This file
├── test-prompts.json     ← Evaluation prompts
├── test-results.md       ← QA results
└── references/
    └── fog-index.py      ← Gunning Fog readability calculator
```

The skill is organized as a **Two-Layer Model**:

| Layer | Focus | Source |
|-------|-------|--------|
| **Layer 1: Strategy** | Reader analysis, gap, contribution, structure | Lebrun |
| **Layer 2: Craft** | Energy, flow, precision, length | Alley |

Plus **7 workflows** covering: writing from scratch, revising, abstract, introduction, sentence audit, title, and conclusion.

## How to Use

1. Load `SKILL.md` into an AI agent that supports skill-based instructions
2. Start with **Layer 1** → fill in the Reader Analysis Worksheet
3. Pick the relevant workflow for your current task
4. Run the workflow's checklist; if the 🔁 loop check reveals a structural mismatch, return to Layer 1

See the **Recommended Reading Order** section in SKILL.md for guidance on sequencing the workflows.


