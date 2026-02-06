# 🚀 Getting Started con IdeaFlow

Benvenuto in IdeaFlow! Questa guida ti accompagnerà passo-passo nel tuo primo utilizzo del framework.

## 🎯 Cosa Imparerai

- Come installare e configurare IdeaFlow
- Come catturare la tua prima idea
- Come seguire il workflow completo
- Come personalizzare il framework per le tue esigenze

## ⚡ Quick Start (5 minuti)

### 1. Clone Repository# 🚀 Getting Started con IdeaFlow

Benvenuto in IdeaFlow! Questa guida ti accompagnerà passo-passo nel tuo primo utilizzo del framework.

## 🎯 Cosa Imparerai

- Come installare e configurare IdeaFlow
- Come catturare la tua prima idea
- Come seguire il workflow completo
- Come personalizzare il framework per le tue esigenze

## ⚡ Quick Start (5 minuti)

### 1. Clone Repository

```bash
git clone https://github.com/disoardi/ideaflow.git
cd ideaflow
```

### 2. Crea il Tuo Spazio Idee

```bash
# Opzione A: Dentro il repository (per test)
mkdir my-ideas
cd my-ideas

# Opzione B: Directory separata (raccomandato)
mkdir ~/ideas
cd ~/ideas
```

### 3. Copia Template Base

```bash
# Dalla directory ideaflow
cp templates/core/idea-tracker.md ~/ideas/
cp -r templates/prompts ~/ideas/
```

### 4. Cattura Prima Idea

Apri `prompts/01-capture.md`, copia il prompt e usalo con il tuo AI preferito (Claude, ChatGPT, etc.).

✅ **Fatto!** Hai catturato la tua prima idea.

---

## 📚 Tutorial Completo

### Fase 0: Setup Iniziale

#### Cosa Ti Serve

- Un editor markdown (VS Code, Obsidian, Silverbullet, etc.)
- Accesso a un AI (Claude, ChatGPT, Gemini, etc.)
- 30 minuti di tempo

#### Setup Directory

Crea questa struttura:

```
ideas/
├── idea-tracker.md          # Tracker principale
├── ideas/                   # Idee individuali
│   ├── idea-001-raw.md
│   ├── idea-001-elaborated.md
│   └── idea-001-complete.md
├── artifacts/               # Materiali implementation
│   └── idea-001/
├── prompts/                 # Prompt IdeaFlow
└── templates/               # Template custom (opzionale)
```

### Fase 1: CAPTURE - Cattura Prima Idea

**Tempo:** 10-15 minuti

#### Step 1: Apri Prompt Capture

Apri file `prompts/01-capture.md` e leggi le istruzioni.

#### Step 2: Pensa alla Tua Idea

Rispondi a queste domande mentalmente:
- Cosa voglio creare/risolvere?
- Per chi sarebbe utile?
- Perché mi interessa?

#### Step 3: Usa il Prompt

1. Copia il prompt da `01-capture.md`
2. Sostituisci `[TUA DESCRIZIONE GREZZA]` con la tua idea
3. Incolla nella conversazione con il tuo AI
4. Rispondi alle domande dell'AI

#### Step 4: Salva Output

1. Salva la risposta dell'AI in `ideas/idea-001-raw.md`
2. Apri `idea-tracker.md`
3. Aggiungi entry nella tabella:

```markdown
| #001 | [Titolo Tua Idea] | 🟠 Captured | 2025-01-28 | Da elaborare |
```

4. Aggiungi sezione dettaglio sotto:

```markdown
### Idea #001: [Titolo]

**📅 Data:** 2025-01-28
**🏷️ Categoria:** [Tech/Personal/Creative/Business]
**🎯 Stato:** 🟠 Captured

#### Descrizione Breve
[2-3 frasi dalla fase capture]

#### Prossimi Step
- [ ] Fase ELABORATE
```

✅ **Prima idea catturata!** 🎉

### Fase 2: ELABORATE - Approfondisci

**Tempo:** 30-45 minuti

**Quando farlo:** Non subito! Lascia passare almeno qualche ora o un giorno. Dà tempo all'idea di "maturare".

#### Step 1: Review Idea Raw

Rileggi `idea-001-raw.md`. Ti convince ancora? Bene, procedi.

#### Step 2: Usa Prompt Elaborate

1. Apri `prompts/02-elaborate.md`
2. Copia il prompt
3. Allega il file `idea-001-raw.md` alla conversazione
4. Rispondi onestamente alle domande dell'AI

**Pro tip:** Prenditi tempo. Le risposte che dai qui determinano la qualità dell'elaborazione.

#### Step 3: Salva Output

1. Salva in `ideas/idea-001-elaborated.md`
2. Aggiorna tracker:
   - Stato: 🟠 → 🟡 In Elaboration
3. Review l'elaborazione prodotta

#### Step 4: Decision Point

Dopo aver letto l'elaborazione, chiediti:
- Mi convince ancora?
- Vale la pena continuare?
- Ho elementi per decidere?

Se sì → Procedi a VALIDATE  
Se no → Stato: 🔴 On Hold o ⚫ Rejected

### Fase 3: VALIDATE - Decidi

**Tempo:** 20-30 minuti

**Obiettivo:** Prendere decisione informata: GO / NO-GO / LATER

#### Step 1: Usa Prompt Validate

1. Apri `prompts/03-validate.md`
2. Allega `idea-001-elaborated.md`
3. Rispondi alle domande di validazione

**Nota:** Questa è la fase critica. Sii onesto con te stesso.

#### Step 2: Salva e Analizza

1. Salva output in `ideas/idea-001-validated.md`
2. Leggi attentamente l'analisi
3. Guarda i punteggi e raccomandazioni

#### Step 3: DECIDI (TU, non l'AI!)

L'AI ti dà analisi, ma **tu decidi**:

**Se GO (✅):**
- Stato: 🔵 To Do
- Procedi a fase DOCUMENT

**Se NO-GO (❌):**
- Stato: ⚫ Rejected
- Documenta perché in nota tracker
- **NON cancellare** - potresti tornarci

**Se LATER (⏸️):**
- Stato: 🔴 On Hold
- Setta reminder review (es. 3 mesi)
- Documenta quando revieware

#### Step 4: Aggiorna Tracker

```markdown
| #001 | [Titolo] | 🔵 To Do | 2025-01-28 | Validated, ready for doc |
```

### Fase 4: DOCUMENT - Documenta

**Tempo:** 1-2 ore

**Quando farlo:** Se hai deciso GO nella fase VALIDATE.

#### Step 1: Usa Prompt Document

1. Apri `prompts/04-document.md`
2. Allega TUTTI i file precedenti (raw, elaborated, validated)
3. Segui il prompt per generare documentazione completa

**Pro tip:** Questa fase richiede concentrazione. Blocca 1-2 ore senza interruzioni.

#### Step 2: Salva e Review

1. Salva output in `ideas/idea-001-complete.md`
2. Leggi tutta la documentazione generata
3. Verifica completezza (usa checklist nel prompt)
4. Aggiungi/modifica parti mancanti

#### Step 3: Genera Diagrammi (se necessari)

Se la documentazione include diagrammi Mermaid/PlantUML:
1. Crea directory `ideas/diagrams/`
2. Salva diagrammi in file separati
3. Renderizza in PNG (usando tool online o local)
4. Link nella documentazione

#### Step 4: Aggiorna Tracker

```markdown
| #001 | [Titolo] | 🔵 Documented | 2025-01-28 | Ready for artifacts |
```

### Fase 5: PREPARE - Genera Artifacts

**Tempo:** 30-45 minuti

**Obiettivo:** Avere materiali pronti per iniziare implementazione.

#### Step 1: Usa Prompt Prepare

1. Apri `prompts/05-prepare.md`
2. Allega `idea-001-complete.md`
3. Chiedi di generare tutti gli artifact

#### Step 2: Organizza Artifacts

1. Crea directory `artifacts/idea-001/`
2. Salva tutti i file generati seguendo struttura suggerita
3. Crea `artifacts/idea-001/README.md` con indice

#### Step 3: Review Artifacts

Verifica di avere:
- ✅ claude.md (se usi Claude Code)
- ✅ Prompt sequence per implementation
- ✅ Checklist implementation
- ✅ Getting started guide
- ✅ Template configurazioni

#### Step 4: SEI PRONTO! 🚀

Aggiorna tracker:
```markdown
| #001 | [Titolo] | 🟢 Ready to Implement | 2025-01-28 | All set! |
```

**Ora puoi iniziare l'implementazione seguendo i materiali generati!**

---

## 🎯 Workflow Visuale

```
💡 Idea Grezza
    ↓
📝 CAPTURE (10-15 min)
    ↓
🟠 Captured
    ↓
[Pausa per maturare]
    ↓
🔍 ELABORATE (30-45 min)
    ↓
🟡 Elaborating
    ↓
✅ VALIDATE (20-30 min)
    ↓
[Decision Point]
    ├→ ❌ NO-GO → ⚫ Rejected
    ├→ ⏸️ LATER → 🔴 On Hold
    └→ ✅ GO
        ↓
📚 DOCUMENT (1-2 hours)
        ↓
🔵 Documented
        ↓
🚀 PREPARE (30-45 min)
        ↓
🟢 Ready to Implement
        ↓
⚙️ IMPLEMENTATION
        ↓
🎉 Done!
```

---

## 💡 Tips per Principianti

### Tip 1: Non Over-Think nella Fase Capture
Cattura l'idea anche se non è perfetta. Elaborerai dopo.

### Tip 2: Usa Timer
Ogni fase ha tempo suggerito. Usa timer per rimanere focused.

### Tip 3: Non Saltare Validate
È la fase più importante. Evita di investire tempo in idee non validate.

### Tip 4: Revisiona Periodicamente
Weekly review del tracker. Aggiorna stati, chiudi idee morte.

### Tip 5: Sii Onesto con Te Stesso
L'AI ti aiuta, ma le decisioni sono tue. Sii critico e realistico.

---

## ❓ Domande Frequenti

### Q: Devo seguire tutte e 5 le fasi?
**A:** Per idee importanti, sì. Per idee minori, puoi fermarti dopo ELABORATE o VALIDATE.

### Q: Quanto tempo tra una fase e l'altra?
**A:** Capture → Elaborate: almeno qualche ora. Elaborate → Validate: immediato o giorno dopo. Validate → Document: quando deciso GO. Document → Prepare: immediato.

### Q: Posso usare AI diversi per fasi diverse?
**A:** Sì! I prompt sono agnostici. Ma mantieni consistenza nello stesso progetto.

### Q: E se cambio idea dopo VALIDATE?
**A:** Normale! Aggiorna stato (es. da To Do a On Hold) e documenta perché.

### Q: Devo creare artifacts anche se implemento subito?
**A:** Sì, ti aiuteranno durante implementazione. Sono una guida, non overhead.

---

## 🎓 Prossimi Step

Ora che sai usare IdeaFlow:

1. ✅ Cattura 2-3 idee per fare pratica
2. ✅ Elabora almeno una fino a VALIDATE
3. ✅ Leggi [Best Practices](best-practices.md)
4. ✅ Personalizza template per tue esigenze
5. ✅ Condividi feedback nella [Community](https://github.com/disoardi/ideaflow/discussions)

---

**Buon IdeaFlowing! 🌊**

*Need help? [Open an issue](https://github.com/disoardi/ideaflow/issues)*
