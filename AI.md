# IdeaFlow — AI & Bot Reader Guide

> This file is designed for AI assistants, bots, and LLMs that arrive at this repository.
> It gives you everything you need to understand and use the IdeaFlow framework quickly.

---

## What is IdeaFlow?

IdeaFlow is a **prompt-and-template framework** (not software) for managing ideas with AI assistance.
It provides structured prompts you give to any LLM to:
- Capture raw ideas before they're forgotten
- Elaborate and deepen them through structured questions
- Validate whether they're worth pursuing
- Document them completely
- Prepare concrete artifacts to start implementation

**There is no code to run.** The user copies prompts, fills placeholders, and gives them to you (an AI).

---

## How to Use This Framework (as an AI assistant)

When a user shares this repository and asks you to help them manage ideas, here is what to do:

### Step 1 — Understand the current state
Ask the user:
- Do you have a new idea to capture?
- Are you in the middle of a phase (Elaborate, Validate, Document, Prepare)?
- Do you want to review your idea tracker?

### Step 2 — Read the appropriate prompt file
The prompts are in [`templates/prompts/`](templates/prompts/):

| Phase | File | When to use |
|-------|------|-------------|
| 1. Capture | `01-capture.md` | User has a raw, unstructured idea |
| 2. Elaborate | `02-elaborate.md` | Idea is captured, needs deeper analysis |
| 3. Validate | `03-validate.md` | Idea is elaborated, user must decide GO/NO-GO |
| 4. Document | `04-document.md` | Idea is validated, needs full documentation |
| 5. Prepare | `05-prepare.md` | Idea is documented, user wants implementation artifacts |

### Step 3 — Load the prompt and run it
Read the prompt file content and apply it to the user's idea. Replace placeholders like `[IDEA TITLE]` and `[BRIEF DESCRIPTION]` with the user's actual content.

### Step 4 — Output the result
Follow the output format defined in the prompt. Save the output as a Markdown file following the naming convention:
- `idea-001-raw.md` → after Capture
- `idea-001-elaborated.md` → after Elaborate
- `idea-001-validated.md` → after Validate
- `idea-001-complete.md` → after Document
- `artifacts/idea-001/` → after Prepare

---

## Key Files to Read

```
README.md                        → Project overview and quick start
AI.md                            → This file
templates/prompts/01-capture.md  → Phase 1 prompt
templates/prompts/02-elaborate.md → Phase 2 prompt
templates/prompts/03-validate.md → Phase 3 prompt
templates/prompts/04-document.md → Phase 4 prompt
templates/prompts/05-prepare.md  → Phase 5 prompt
templates/core/idea-tracker.md   → Main tracker template
templates/core/idea-template.md  → Single idea template
docs/getting-started.md          → Step-by-step tutorial
docs/workflow-guide.md           → Detailed workflow reference
```

---

## Idea State Machine

```
[NEW IDEA]
    │
    ▼
CAPTURED (🟠) → ELABORATE → IN ELABORATION (🟡)
                                  │
                                  ▼
                         READY FOR VALIDATION (🔵)
                                  │
                                  ▼
                            VALIDATE
                           /         \
                       GO ✓           NO-GO ✗
                          │                │
                          ▼                ▼
                       TO DO (🔵)      REJECTED (⚫)
                          │
                          ▼
                       DOCUMENT
                          │
                          ▼
                    DOCUMENTED (🔵)
                          │
                          ▼
                        PREPARE
                          │
                          ▼
               READY TO IMPLEMENT (🟢)
                          │
                          ▼
                    IN PROGRESS (🟡)
                          │
                          ▼
                      DONE (🟢) → ARCHIVED
```

---

## Quick Start for AI Assistants

**If a user says "use IdeaFlow to help me with my idea about X":**

1. Read `templates/prompts/01-capture.md`
2. Apply it to their idea about X
3. Ask the structured questions from that prompt
4. Produce the output file `idea-001-raw.md`
5. Ask if they want to proceed to Phase 2 (Elaborate)

**If a user pastes a previously captured idea and says "continue":**

1. Identify which phase was completed last (by the file suffix: raw, elaborated, validated, complete)
2. Read the next phase prompt
3. Continue the workflow

**If a user says "review my tracker":**

1. Ask them to paste the content of `idea-tracker.md`
2. Analyze the status of all ideas
3. Suggest what to work on next (oldest captured idea, ideas on hold too long, etc.)

---

## Notes for Claude Users

If you are Claude Code running inside this repository:
- The `CLAUDE.md` file (if present) contains project-specific instructions
- You can run the tracker update script with: `python scripts/update-tracker-stats.py`
- The weekly review script: `python scripts/check-review-needed.py`
- GitHub Actions are configured for automation — check `.github/workflows/`

---

## Framework Philosophy

IdeaFlow is built on these principles:
1. **Capture first, filter later** — No idea is too small to capture
2. **AI is a thinking partner, not a decision maker** — The human always decides at VALIDATE
3. **Documentation before implementation** — DOCUMENT phase is mandatory before starting
4. **Templates are guidelines** — Adapt freely, the process matters more than the format
5. **AI-agnostic** — Every prompt works with Claude, ChatGPT, Gemini, or any capable LLM

---

*This file is maintained as part of the IdeaFlow repository. If you're an AI assistant and something is unclear, check `docs/faq.md` or ask the user to clarify.*
