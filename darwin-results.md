# Darwin Skill 2.0 Evaluation — scientific-paper-writing

**Generated:** 2026-07-30
**Skill:** `books/scientific-paper-writing/scientific-paper-writing/SKILL.md`
**Method:** Dry run (sub-agent unavailable → self-evaluation with darwin-skill v2.0 rubric)

---

## Final Score: 94.7 / 100

| # | Dimension | Score | Weight | Weighted | Δ from Baseline |
|---|-----------|-------|--------|----------|-----------------|
| 1 | Frontmatter Quality | **10** | 7 | 70 | +1 |
| 2 | Workflow Clarity | **9** | 12 | 108 | +1 |
| 3 | Failure Mode Encoding | **10** | 12 | 120 | +1 |
| 4 | Checkpoint Design | **10** | 6 | 60 | +5 |
| 5 | Actionable Specificity | **10** | 17 | 170 | 0 |
| 6 | Resource Integration | **8** | 4 | 32 | +2 |
| 7 | Overall Architecture | **10** | 12 | 120 | 0 |
| 8 | Effectiveness (dry run) | **9** | 23 | 207 | 0 |
| 9 | Anti-Examples & Blacklist | **10** | 6 | 60 | 0 |
| | **Total** | | **100** | **947** | **+69** |

---

## Baseline → Final Comparison

```
                          Baseline    Optimized    Δ
                          ─────────   ─────────   ───
Dim1 Frontmatter             9/10       10/10     +1
Dim2 Workflow Clarity        8/10        9/10     +1
Dim3 Failure Mode            9/10       10/10     +1
Dim4 Checkpoint Design       5/10       10/10     +5  ◄ most improved
Dim5 Actionable Specificity 10/10       10/10      —
Dim6 Resource Integration    6/10        8/10     +2
Dim7 Architecture           10/10       10/10      —
Dim8 Effectiveness            9/10        9/10      —
Dim9 Anti-Examples          10/10       10/10      —
                          ─────────   ─────────   ───
Total:                      87.8        94.7     +6.9
```

---

## Optimization Iterations (6)

| Iter | Change | Target | Δ Score |
|------|--------|--------|---------|
| **1** | 🔁 agent self-checks → 🔴 STOP + user decision tables (all 7 workflows) | Dim4: 5→8 | +18 |
| **2** | I/O annotations on all 7 workflows (Input → Output) | Dim2: 8→9 | +12 |
| **3** | Failure Modes + When NOT → structured if-then tables | Dim3: 9→10 | +12 |
| **4** | Frontmatter `related_skills` populated (8 skills) | Dim1: 9→10 | +7 |
| **5** | Bundled `references/fog-index.py` utility script | Dim6: 6→8 | +8 |
| **6** | Centralized Checkpoint Summary table + user response guide | Dim4: 8→10 | +12 |

### Git Log

```
bf66855 iter6: Add centralized Checkpoint Summary table
9663e67 iter5: Bundle references/fog-index.py as reusable resource
1cc0770 iter4: Populate related_skills in frontmatter
80c2262 iter3: Convert failure modes and when-NOT-to-use to if-then tables
92401f2 iter2: Add explicit Input/Output annotations to all 7 workflows
9a7e562 iter1: Upgrade all checkpoints from agent-self-check to user-confirmation
51dd0f3 Add README for scientific-paper-writing skill
aba6eeb Initial commit: scientific writing skill knowledge base
```

---

## Strengths (at final)

1. **Two-Layer Model** (Strategy + Craft) unifies 7 workflows under a coherent framework
2. **Checkpoint system** — all 7 workflows have 🔴 STOP markers with user-facing decision tables + centralized summary
3. **Sentence Audit (W5)** — operationalizes abstract concepts (energy, flow, emphasis) into executable checks
4. **Counter-Examples & Key Cases** — 8 real cases + explicit trap→spot→fix tables
5. **Exceptionally specific** — no banned AI-filler phrases, 14+ explicit checklists/tables/equations

## Remaining Gaps

| Dim | Current | Potential | Expected Gain |
|-----|---------|-----------|---------------|
| 6 - Resource Integration | 8 | 10 | +8 |
| 8 - Effectiveness | 9 | 10 | +23 |

- **Dim6**: Add more reference scripts/templates (e.g., a paragraph-level revision worksheet)
- **Dim8**: Requires running 16 test prompts through actual agent execution and verifying output quality
