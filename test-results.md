# Test Results — scientific-paper-writing

> Generated: 2026-07-30 (placeholder)
> Tests defined in: test-prompts.json (16 tests: 8 should-trigger, 5 should-not-trigger, 3 boundary)
> Status: Pending darwin-skill evaluation

## Summary

| Category | Total | Passed | Failed | Pending |
|----------|-------|--------|--------|---------|
| Should Trigger | 8 | — | — | 8 |
| Should Not Trigger | 5 | — | — | 5 |
| Boundary | 3 | — | — | 3 |
| **Total** | **16** | **—** | **—** | **16** |

## Instructions for darwin-skill

Run these tests using darwin-skill's evaluation framework:

```bash
darwin evolve books/scientific-paper-writing/
```

Each test in `test-prompts.json` will be evaluated by an independent judge agent.
Test results will be written here after evaluation.

## Test Categories

### Should Trigger (8)
Prompts that should activate this skill for scientific paper writing assistance:
- Writing a paper from data
- Revising an abstract
- Restructuring an introduction
- Improving methods section (Chinese)
- Pre-submission quality check
- Discussion section improvement
- Audience analysis
- Chinese paragraph improvement

### Should NOT Trigger (5) — Bait
Prompts that look related but belong to other skills:
- Figure creation → nature-figure
- Reference search → nature-citation
- LaTeX formatting → not this skill
- Reviewer response → nature-response
- De-AI-ing → humanizer

### Boundary (3)
Ambiguous cases that may require partial activation:
- Grammar check only (partial)
- News writing (adjacent)
- Grant proposal (partial overlap)
