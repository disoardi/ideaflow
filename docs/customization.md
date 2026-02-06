# 🎨 Customization Guide - IdeaFlow

Come personalizzare IdeaFlow per le tue esigenze.

## 🎯 Filosofia

IdeaFlow è un **framework**, non un tool rigido. È pensato per essere:
- ✅ Personalizzabile
- ✅ Estendibile
- ✅ Adattabile

**Regola d'oro:** Se qualcosa non funziona per te, cambiala!

---

## 📝 Customizzare Template

### Template Esistenti

IdeaFlow fornisce:
- `idea-tracker.md` - Tracker principale
- `idea-template.md` - Template singola idea
- Prompt 01-05 - Prompt per le 5 fasi

### Creare Template Custom

**Scenario:** Hai use case specifico (es. research paper, saas idea, learning project)

**Come fare:**

1. Copia template base:
```bash
cp templates/core/idea-template.md templates/my-templates/research-paper.md
```

2. Modifica sezioni:
```markdown
# 💡 Research Paper: [Titolo]

## 📚 Research Context
[Sezioni specifiche per research]

## 🔬 Methodology
[Come fare la ricerca]

## 📊 Expected Results
[Cosa ti aspetti di trovare]
```

3. Usa template custom quando catturi idea di quel tipo

**Esempi Template Custom:**

**SaaS Product:**
```markdown
# 💡 SaaS Idea: [Nome]

## 💰 Business Model
- Pricing: [How]
- Target Customer: [Who]
- CAC / LTV: [Estimates]

## 🎯 Market Analysis
- Market Size: [TAM/SAM/SOM]
- Competitors: [Who]
- Differentiation: [Why us]

## 📈 Growth Strategy
[How to grow]
```

**Learning Project:**
```markdown
# 💡 Learning: [Skill/Technology]

## 🎓 Learning Goals
- Skill level target: [Beginner/Intermediate/Advanced]
- Time commitment: [Hours/week]
- Success criteria: [How I know I learned]

## 📚 Resources
- Courses: [List]
- Books: [List]
- Projects to build: [List]

## ⏱️ Timeline
[Week by week plan]
```

---

## 🎨 Customizzare Stati

### Stati Default

```yaml
# states-config.yaml (default)
states:
  captured:
    icon: "🟠"
    name: "Captured"
    description: "Idea catturata, da elaborare"
    
  in_progress:
    icon: "🟡"
    name: "In Progress"
    description: "Implementation in corso"
    
  # ... etc
```

### Aggiungere Stati Custom

**Scenario:** Vuoi stati intermedi o specifici per tuo workflow

**Esempio:**
```yaml
# my-states-config.yaml
states:
  # Stati default
  captured:
    icon: "🟠"
    
  # Stati custom
  in_research:
    icon: "🔍"
    name: "In Research"
    description: "Ricerca preliminare in corso"
    
  prototype:
    icon: "⚗️"
    name: "Prototype"
    description: "Prototype/MVP in sviluppo"
    
  beta:
    icon: "🧪"
    name: "Beta"
    description: "In beta testing"
    
  launched:
    icon: "🚀"
    name: "Launched"
    description: "Lanciato in produzione"
```

### Workflow con Stati Custom

```
Captured → In Research → Validated → Prototype → Beta → Launched → Done
```

---

## 🎯 Customizzare Prompt

### Modificare Prompt Esistenti

**Scenario:** Prompt standard non fanno domande rilevanti per te

**Come fare:**

1. Copia prompt:
```bash
cp templates/prompts/02-elaborate.md prompts/my-elaborate.md
```

2. Modifica sezioni:
```markdown
# 🔍 My Custom ELABORATE Prompt

[Mantieni struttura base ma cambia domande]

### 1. 🎯 My Custom Questions

- [Domanda specifica per il tuo dominio]
- [Altra domanda custom]
```

3. Usa prompt custom al posto di quello standard

### Aggiungere Nuove Fasi

**Scenario:** Vuoi fase aggiuntiva tra VALIDATE e DOCUMENT

**Esempio: Fase PROTOTYPE**

```markdown
# ⚗️ Prompt Fase 2.5: PROTOTYPE

> Usa questo prompt per creare quick prototype prima di documentare.

## 💬 PROMPT

Dopo aver validato questa idea, voglio fare quick prototype:

[INCOLLA idea-XXX-validated.md]

Aiutami a:

1. Definire MVP minimo per prototype (max 2 giorni effort)
2. Identificare core feature da testare
3. Suggerire stack tecnologico per rapid prototyping
4. Generare checklist rapida implementation
5. Definire success criteria per prototype

Output: Piano prototype pratico, ready to code.
```

**Workflow custom:**
```
CAPTURE → ELABORATE → VALIDATE → PROTOTYPE → DOCUMENT → PREPARE
```

---

## 🏷️ Sistema di Tag

### Tag Custom

Aggiungi tag per categorizzare meglio:

```markdown
# Idea Tracker

## 🏷️ Tag Categories

**By Domain:**
`#tech` `#business` `#creative` `#personal` `#research`

**By Effort:**
`#quick-win` `#medium` `#large` `#marathon`

**By Impact:**
`#high-impact` `#medium-impact` `#low-impact`

**By Type:**
`#tool` `#product` `#content` `#learning` `#experiment`

**Custom:**
`#ai-powered` `#web-app` `#mobile` `#saas` `#open-source`
```

### Usare Tag

```markdown
### Idea #001: My Tool

**📅 Data:** 2025-01-28
**🏷️ Tag:** `#tech` `#tool` `#quick-win` `#high-impact` `#ai-powered`
```

### Filtrare per Tag

Search nel tracker per tag specifici:
- Cerchi `#quick-win` → Trovi tutte le quick win
- Cerchi `#high-impact AND #quick-win` → Sweet spot!

---

## 📊 Customizzare Metriche

### Metriche Default

IdeaFlow traccia:
- Numero idee per stato
- Conversion rate tra fasi
- Time per fase

### Aggiungere Metriche Custom

**Scenario:** Vuoi tracciare metriche specifiche

**Esempio:**

```markdown
# Idea Tracker

## 📊 My Custom Metrics

### ROI Tracking
| Idea | Time Invested | Value Created | ROI |
|------|---------------|---------------|-----|
| #001 | 20h | High | ⭐⭐⭐⭐⭐ |
| #002 | 5h | Low | ⭐⭐ |

### Learning Tracker
| Idea | Skills Learned | Applicability |
|------|---------------|---------------|
| #001 | React, Three.js | High |
| #003 | Ansible, CDP | Medium |

### Impact Score
[Your custom scoring system]
```

---

## 🔧 Workflow Customizations

### Workflow Variazioni

**Lightweight Workflow** (per idee semplici):
```
CAPTURE → VALIDATE → IMPLEMENT
(Skip: ELABORATE, DOCUMENT, PREPARE)
```

**Heavy Research Workflow**:
```
CAPTURE → RESEARCH → ELABORATE → VALIDATE → PROTOTYPE → TEST → DOCUMENT → PREPARE
```

**Collaborative Workflow**:
```
CAPTURE → ELABORATE → PEER_REVIEW → VALIDATE → DOCUMENT → PREPARE
```

### Configurare Workflow

Documenta il tuo workflow custom:

```markdown
# My Custom Workflow

## For Quick Ideas (<1 day effort)
CAPTURE → VALIDATE → IMPLEMENT

## For Medium Projects (1-2 weeks)
CAPTURE → ELABORATE → VALIDATE → PREPARE → IMPLEMENT

## For Large Projects (1+ months)
Full workflow + PROTOTYPE phase
```

---

## 🤖 Customizzare AI Interaction

### Multi-AI Strategy

Usa AI diversi per fasi diverse:

```
CAPTURE: ChatGPT (veloce)
ELABORATE: Claude (profondo)
VALIDATE: Gemini (prospettive diverse)
DOCUMENT: Claude (strutturato)
PREPARE: ChatGPT (generazione artifacts)
```

### Prompt Engineering Custom

Adatta prompt al tuo AI preferito:

**Per ChatGPT:**
```markdown
You are an expert idea elaborator. Focus on:
- Concrete examples
- Step-by-step breakdown
- Actionable insights
```

**Per Claude:**
```markdown
Take a comprehensive analytical approach:
- Consider multiple perspectives
- Identify edge cases
- Provide nuanced analysis
```

---

## 📁 Directory Structure Custom

### Structure Alternative

**Opzione 1: Per Categoria**
```
ideas/
├── tech/
│   ├── tracker-tech.md
│   └── ideas/
├── personal/
│   ├── tracker-personal.md
│   └── ideas/
└── business/
    ├── tracker-business.md
    └── ideas/
```

**Opzione 2: Per Anno**
```
ideas/
├── 2025/
│   ├── tracker-2025.md
│   └── ideas/
└── 2026/
    ├── tracker-2026.md
    └── ideas/
```

**Opzione 3: Per Stato**
```
ideas/
├── active/       # In Progress
├── backlog/      # Captured, To Do
├── completed/    # Done
└── archive/      # On Hold, Rejected
```

---

## 🔄 Integration con Altri Tool

### Obsidian Integration

```markdown
# In Obsidian
- Usa dataview per query dinamiche
- Link wiki-style tra idee
- Graph view per visualizzare collegamenti
```

**Esempio Dataview:**
```dataview
TABLE status, category, date
FROM "ideas"
WHERE status = "In Progress"
SORT date DESC
```

### Notion Integration

```markdown
# In Notion
- Database per idee
- Properties: Status, Category, Priority, etc.
- Views: Kanban, Timeline, Calendar
```

### VS Code Integration

```markdown
# In VS Code
- Workspace per ideas
- Markdown All in One extension
- Mermaid Preview
- TODO Highlight
```

---

## 🎨 Visual Customizations

### Custom Icons

Cambia icon per stati:

```yaml
states:
  captured: "💡"    # Invece di 🟠
  done: "✅"         # Invece di 🟢
  rejected: "❌"     # Invece di ⚫
```

### Color Coding

Se usi Obsidian/Notion, aggiungi colori:

```markdown
**🟢 Done** → Verde
**🟡 In Progress** → Giallo
**🔵 To Do** → Blu
**🔴 On Hold** → Rosso
**⚫ Rejected** → Grigio
```

---

## 📋 Checklist Customizations

### Custom Checklists

Aggiungi checklist specifiche per tuo workflow:

```markdown
# My Custom Checklists

## Pre-Implementation Checklist
- [ ] Discussed with team
- [ ] Budget approved
- [ ] Timeline agreed
- [ ] Resources allocated
- [ ] Risks documented

## Post-Implementation Checklist
- [ ] User feedback collected
- [ ] Metrics tracked
- [ ] Documentation updated
- [ ] Learnings documented
- [ ] Celebration! 🎉
```

---

## 🚀 Framework Extensions

### Plugin System (Future)

Crea "plugin" per funzionalità custom:

```
plugins/
├── auto-tagging/          # Auto-suggest tag
├── ai-similarity/         # Trova idee simili
└── metrics-dashboard/     # Dashboard metriche
```

### Automation Scripts

Automatizza task ripetitivi:

```bash
# scripts/weekly-review.sh
#!/bin/bash
# Genera report automatico idee per weekly review

echo "## Weekly Idea Review"
echo "Date: $(date)"
grep "🟠 Captured" idea-tracker.md
grep "🟡 In Progress" idea-tracker.md
```

---

## 💡 Custom Use Cases

### Use Case 1: Content Creator

**Workflow:**
```
CAPTURE (Content idea)
    ↓
ELABORATE (Outline)
    ↓
SCRIPT (Custom phase - write script)
    ↓
PRODUCE (Create content)
    ↓
PUBLISH
```

**Custom Template:**
```markdown
# Content Idea: [Title]

## 📹 Format
[Video/Article/Podcast/etc.]

## 🎯 Target Audience
[Who]

## 💡 Key Message
[What]

## 📋 Outline
[Structure]

## 📊 Success Metrics
[Views/Shares/etc.]
```

### Use Case 2: Researcher

**Custom Phases:**
```
CAPTURE → LITERATURE_REVIEW → HYPOTHESIS → METHODOLOGY → EXPERIMENT → DOCUMENT → PUBLISH
```

### Use Case 3: Product Manager

**Custom Template:**
```markdown
# Product Feature: [Name]

## 👥 User Story
As a [user], I want [feature] so that [benefit]

## 📊 Business Metrics
- Impact on revenue: [Estimate]
- User adoption target: [%]
- Success criteria: [Metrics]

## 🔧 Technical Feasibility
[Effort estimate, dependencies]
```

---

## 🤝 Sharing Customizations

### Contribute Back

Se crei customization utile:
1. Documenta bene
2. Testa con 3+ idee
3. Condividi via PR o Discussion

**Template PR:**
```markdown
## New Template: [Nome]

**Use Case:** [Scenario]
**Why Useful:** [Ragionamento]
**Tested:** Yes, on 5 ideas
**Documentation:** Complete

[Link to template file]
```

---

## 📚 Examples Repository

IdeaFlow community sta creando repository di customization:
- Custom templates
- Workflow variations
- Integration scripts
- Automation tools

**Check:** `examples/customizations/` per idee

---

**Remember: IdeaFlow è tuo. Modificalo senza paura!**

Se crei qualcosa di utile, condividilo con la community! 🚀
