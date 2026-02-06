# 🎯 Esempio Workflow Completo

Questo esempio mostra l'intero workflow IdeaFlow applicato a un'idea fittizia.

**Idea Esempio:** "App Mobile per Tracking Abitudini con AI"

> **📝 Nota:** Questo esempio usa Claude come AI assistant e include riferimenti specifici (es. `claude.md`, Claude API).
> IdeaFlow funziona con qualsiasi LLM - adatta i riferimenti al tuo AI preferito (es. `ai-context.md` invece di `claude.md`).

---

## 📁 File in Questo Esempio

```
complete-workflow/
├── README.md                    # Questo file
├── 01-capture-output.md         # Output fase CAPTURE
├── 02-elaborate-output.md       # Output fase ELABORATE
├── 03-validate-output.md        # Output fase VALIDATE
├── 04-document-output.md        # Output fase DOCUMENT
├── 05-artifacts/                # Output fase PREPARE
│   ├── claude.md
│   ├── prompts/
│   ├── checklists/
│   └── README.md
└── tracker-evolution.md         # Come evolve il tracker
```

---

## 🔄 Fase per Fase

### Fase 1: CAPTURE

**Input (idea grezza):**
"Vorrei creare un'app che mi aiuta a tracciare le mie abitudini giornaliere. Tipo Duolingo ma per qualsiasi abitudine. Con AI che mi da suggerimenti personalizzati."

**Processo:**
1. Uso prompt `01-capture.md`
2. AI fa domande:
   - Quali abitudini vuoi tracciare?
   - Come l'AI aiuterebbe?
   - Per chi è questa app?
   - Cosa c'è già di simile?
3. Rispondo brevemente
4. AI struttura in formato base

**Output:** `01-capture-output.md` → Idea strutturata

**Tracker Update:**
```markdown
| #001 | Habit Tracker App con AI | 🟠 Captured | 2025-01-28 | Da elaborare |
```

[Vedi file: 01-capture-output.md per output completo]

---

### Fase 2: ELABORATE

**Input:** `01-capture-output.md`

**Processo:**
1. Uso prompt `02-elaborate.md`
2. AI approfondisce 6 aree
3. Rispondo con esempi concreti
4. AI genera analisi dettagliata

**Output:** `02-elaborate-output.md` → 8 sezioni approfondite

**Highlights elaborazione:**
- **Problema:** App esistenti (Habitica, Streaks) troppo generiche, no personalizzazione
- **Soluzione:** AI analizza patterns e suggerisce modifiche personalizzate
- **MVP:** Solo abitudini binarie (fatto/non fatto), 1 AI suggestion al giorno
- **Quick Win:** Prototype in 2 giorni con React Native + local storage

**Tracker Update:**
```markdown
| #001 | Habit Tracker App con AI | 🔵 Ready for Validation | 2025-01-28 | Elaborata |
```

[Vedi file: 02-elaborate-output.md per output completo]

---

### Fase 3: VALIDATE

**Input:** `02-elaborate-output.md`

**Processo:**
1. Uso prompt `03-validate.md`
2. AI guida validation
3. Rispondo onestamente su risorse/tempo
4. AI genera recommendation

**Output:** `03-validate-output.md` → Decision: GO

**Highlights validation:**
- **Quick Test:** Build prototype in 2 giorni → FATTO, funziona
- **Risk:** Keeping users engaged → Mitigazione: gamification
- **Effort:** MVP = 3 settimane
- **Score:** 23/30 (good!)
- **Decision:** GO - procedere con MVP

**Tracker Update:**
```markdown
| #001 | Habit Tracker App con AI | 🔵 To Do | 2025-01-29 | Validated GO, ready for doc |
```

[Vedi file: 03-validate-output.md per output completo]

---

### Fase 4: DOCUMENT

**Input:** Tutti i file precedenti

**Processo:**
1. Uso prompt `04-document.md`
2. AI genera documentazione completa (12 sezioni)
3. Review e aggiungo dettagli
4. Genero diagrammi Mermaid

**Output:** `04-document-output.md` → 35 pagine documentazione

**Highlights documentation:**
- **Architecture:** React Native + Expo, Firebase backend, Claude API
- **Requisiti:** 15 funzionali, 5 non-funzionali
- **Roadmap:** 4 fasi, 6 settimane totali
- **Diagrammi:** App architecture, data model, user flow

**Tracker Update:**
```markdown
| #001 | Habit Tracker App con AI | 🔵 Documented | 2025-01-29 | Ready for artifacts |
```

[Vedi file: 04-document-output.md per output completo]

---

### Fase 5: PREPARE

**Input:** `04-document-output.md`

**Processo:**
1. Uso prompt `05-prepare.md`
2. AI genera 10 tipi di artifacts
3. Organizzo in directory `05-artifacts/`

**Output:** `05-artifacts/` → Materiali pronti

**Artifacts generati:**
- `claude.md` - Context completo per Claude Code
- `prompts/01-setup.md` - Setup React Native project
- `prompts/02-auth.md` - Implement authentication
- `prompts/03-habits.md` - Core habit tracking
- `prompts/04-ai.md` - AI integration
- `checklists/implementation.md` - Checklist 30 task
- `guides/getting-started.md` - Come iniziare development
- `templates/habit-schema.json` - Data model

**Tracker Update:**
```markdown
| #001 | Habit Tracker App con AI | 🟢 Ready to Implement | 2025-01-29 | All set! |
```

[Vedi directory: 05-artifacts/ per tutti i file]

---

## 📊 Tracker Evolution

Come il tracker evolve attraverso le fasi:

**Inizio (Post-CAPTURE):**
```markdown
| #001 | Habit Tracker App | 🟠 Captured | 2025-01-28 | - |
```

**Post-ELABORATE:**
```markdown
| #001 | Habit Tracker App con AI | 🔵 Ready for Validation | 2025-01-28 | Elaborata, promettente |
```

**Post-VALIDATE:**
```markdown
| #001 | Habit Tracker App con AI | 🔵 To Do | 2025-01-29 | Validated GO, score 23/30 |
```

**Post-DOCUMENT:**
```markdown
| #001 | Habit Tracker App con AI | 🔵 Documented | 2025-01-29 | Doc completa, 35 pagine |
```

**Post-PREPARE:**
```markdown
| #001 | Habit Tracker App con AI | 🟢 Ready to Implement | 2025-01-29 | Artifacts ready |
```

**Durante Implementation:**
```markdown
| #001 | Habit Tracker App con AI | 🟡 In Progress | 2025-02-01 | Week 2/6, auth done |
```

**Completata:**
```markdown
| #001 | Habit Tracker App con AI | 🟢 Done | 2025-03-15 | Live on App Store! |
```

---

## 📊 Timeline Esempio

```
Giorno 1:   CAPTURE (15 min)
Giorno 2:   ELABORATE (45 min)
Giorno 3:   VALIDATE (30 min) + Quick Test (2 giorni)
Giorno 5:   DOCUMENT (2 hours)
Giorno 6:   PREPARE (45 min)
Giorno 7:   START Implementation
            ↓
Settimana 2-7: Development (6 settimane)
            ↓
Settimana 8: Launch! 🚀
```

**Totale: Da idea a launch in 8 settimane**
- Pre-implementation: 1 settimana
- Implementation: 6 settimane
- Launch: 1 settimana

---

## 💡 Key Learnings da Questo Esempio

### Learning 1: Quick Test Fondamentale
Il quick test (2 giorni prototype) ha validato:
- ✅ React Native era buona scelta
- ✅ Firebase sufficiente per MVP
- ✅ Users interessati al concept
- ❌ AI suggestions ogni minuto troppo invasive → Pivot a 1/giorno

### Learning 2: Documentation Saves Time
2 ore spese in DOCUMENT hanno risparmiato:
- 5 ore di development confuso
- 3 ore di rework per architecture changes

**ROI:** 1 hour doc = 3-4 hours saved in dev

### Learning 3: Artifacts Guidano Implementation
Seguire checklist e prompts:
- ✅ Niente feature creep
- ✅ Focus su MVP
- ✅ Deadlines rispettate

---

## 🎯 Come Usare Questo Esempio

1. Leggi i file in ordine (01 → 05)
2. Nota come output di ogni fase alimenta la successiva
3. Osserva come il tracker evolve
4. Usa come reference per tue idee

---

*Esempio completo IdeaFlow - Tutti i file disponibili in questa directory*
