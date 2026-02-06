# 🔄 Workflow Guide - IdeaFlow

Guida dettagliata tecnica su come funziona il workflow IdeaFlow.

## 📋 Indice

- [Overview Processo](#overview-processo)
- [Fase 1: CAPTURE](#fase-1-capture)
- [Fase 2: ELABORATE](#fase-2-elaborate)
- [Fase 3: VALIDATE](#fase-3-validate)
- [Fase 4: DOCUMENT](#fase-4-document)
- [Fase 5: PREPARE](#fase-5-prepare)
- [Stati e Transizioni](#stati-e-transizioni)
- [File Organization](#file-organization)

---

## Overview Processo

Il workflow IdeaFlow è un processo **lineare con checkpoint**:

```
CAPTURE → ELABORATE → VALIDATE → DOCUMENT → PREPARE → IMPLEMENT
   ↓          ↓           ↓           ↓          ↓          ↓
  Raw    Elaborated   Validated  Documented  Artifacts   Done
```

**Caratteristiche:**
- **Lineare**: Segui le fasi in ordine
- **Checkpoint**: Puoi fermarti a qualsiasi fase
- **Reversibile**: Puoi tornare indietro e rifare fasi
- **Opzionale**: Non tutte le idee richiedono tutte le fasi

---

## Fase 1: CAPTURE

### Obiettivo
Catturare idea grezza prima che venga dimenticata.

### Input
- Pensiero/idea nella tua testa
- Può essere disordinata, incompleta, vaga

### Processo
1. Apri prompt `01-capture.md`
2. Descrivi idea in linguaggio naturale
3. AI fa domande chiarificatrici (3-5)
4. Rispondi brevemente
5. AI struttura in formato base

### Output
File: `ideas/idea-XXX-raw.md`

Contiene:
- Titolo provvisorio
- Categoria
- Descrizione breve (2-3 paragrafi)
- Obiettivo principale
- Target/beneficiari
- Stima complessità
- Domande aperte per fase ELABORATE

### Tempo
10-15 minuti

### Success Criteria
- ✅ Idea è catturata e non andrà persa
- ✅ C'è abbastanza informazione per decidere se elaborare
- ✅ Domande aperte identificate

### Decisione Post-Fase
**Procedi a ELABORATE?**
- Sì: Se idea promettente
- No: Lascia in stato Captured per review futura

### Note Tecniche
- Non over-think
- Non serve perfezione
- Obiettivo: salvare idea, non raffinarla

---

## Fase 2: ELABORATE

### Obiettivo
Approfondire idea con analisi strutturata.

### Input
- File `idea-XXX-raw.md`
- Tempo disponibile (30-45 min)
- Mente fresca e concentrata

### Processo
1. Review idea raw
2. Apri prompt `02-elaborate.md`
3. AI fa domande dettagliate su 6 aree:
   - Analisi problema
   - Soluzione proposta
   - Fattibilità
   - Impatto
   - Collegamenti
   - Next steps
4. Rispondi in dettaglio (prendi tempo!)
5. AI genera documento elaborato

### Output
File: `ideas/idea-XXX-elaborated.md`

Contiene:
- Executive summary
- Analisi problema dettagliata
- Soluzione proposta con architettura
- Analisi fattibilità
- Impatto atteso
- Alternative considerate
- Roadmap iniziale
- Quick wins
- Domande ancora aperte

### Tempo
30-45 minuti

### Success Criteria
- ✅ Capisco profondamente l'idea
- ✅ Ho identificato rischi e blocchi
- ✅ Ho idea chiara di effort richiesto
- ✅ Posso decidere se procedere

### Decisione Post-Fase
**L'idea convince ancora?**
- Sì: Procedi a VALIDATE
- No: Stato → On Hold o Rejected

### Note Tecniche
- Blocca tempo senza interruzioni
- Sii onesto nelle risposte
- Non avere fretta
- Qualità risposte = qualità elaborazione

---

## Fase 3: VALIDATE

### Obiettivo
Prendere decisione informata: GO / NO-GO / LATER.

### Input
- File `idea-XXX-elaborated.md`
- Contesto personale (tempo, risorse, priorità)
- Obiettività critica

### Processo
1. Apri prompt `03-validate.md`
2. AI guida attraverso:
   - Quick validation test
   - MVP definition
   - Risk assessment
   - Effort vs Impact
   - Priority scoring
   - Go/No-Go recommendation
   - Timeline
3. Rispondi con onestà brutale
4. AI genera validation report con raccomandazione

### Output
File: `ideas/idea-XXX-validated.md`

Contiene:
- Executive summary validazione
- Analisi rischi dettagliata
- Score (1-30)
- **Raccomandazione** (GO/LATER/PIVOT/NO-GO)
- Se GO: Timeline e milestones
- Se NO-GO: Ragionamento e learnings

### Tempo
20-30 minuti

### Success Criteria
- ✅ Ho preso decisione chiara
- ✅ Decisione è supportata da analisi
- ✅ So esattamente cosa fare dopo

### Decisione Post-Fase
**TU decidi** (non l'AI):
- **GO**: Procedi a DOCUMENT
- **LATER**: Stato → On Hold, setta reminder
- **NO-GO**: Stato → Rejected, documenta why

### Note Tecniche
- Questa è la fase più critica
- AI dà raccomandazione, tu decidi
- OK dire NO anche a idee che ami
- On Hold != Rejected

---

## Fase 4: DOCUMENT

### Obiettivo
Creare documentazione completa ready for implementation.

### Input
- Tutti i file precedenti (raw, elaborated, validated)
- Decisione GO dalla fase VALIDATE
- 1-2 ore di tempo disponibile

### Processo
1. Apri prompt `04-document.md`
2. AI genera documentazione strutturata in 12 sezioni:
   - Executive Summary
   - Descrizione Dettagliata
   - Obiettivi e Metriche
   - Architettura/Design
   - Requisiti (funzionali e non)
   - Fasi e Milestone
   - Alternative Considerate
   - Rischi e Mitigazioni
   - Timeline
   - Risorse Necessarie
   - Collegamenti
   - Note
3. Review e integra parti mancanti
4. Genera diagrammi se necessari

### Output
File: `ideas/idea-XXX-complete.md`

Contiene: Documentazione completa pronta per essere usata come reference durante implementation.

Opzionale: `ideas/diagrams/` con diagrammi visuali

### Tempo
1-2 ore

### Success Criteria
- ✅ Documentazione è completa (usa checklist)
- ✅ Chiunque può capire l'idea leggendola
- ✅ Ho roadmap chiara
- ✅ Requisiti sono ben definiti

### Decisione Post-Fase
**Pronto per generare artifacts?**
- Sì: Procedi a PREPARE
- No: Rivedi documentazione, aggiungi mancanze

### Note Tecniche
- Questo è il tuo "contratto" con te stesso
- Servirà da reference durante implementation
- Better over-document che under-document
- Puoi sempre aggiornare durante implementation

---

## Fase 5: PREPARE

### Obiettivo
Generare materiali concreti per iniziare implementation.

### Input
- File `idea-XXX-complete.md`
- Conoscenza di tool/framework da usare

### Processo
1. Apri prompt `05-prepare.md`
2. AI genera 10 tipi di artifact:
   - ai-context.md (context per AI - rinominare in CLAUDE.md se usi Claude)
   - Setup prompts (sequence per development)
   - Repository structure
   - Implementation checklist
   - Testing plan
   - Getting started guide
   - Progress tracker
   - Configuration templates
   - Documentation templates
   - Quick start script
3. Organizza in directory `artifacts/idea-XXX/`

### Output
Directory: `artifacts/idea-XXX/`

Contiene: Tutti i materiali pronti per iniziare implementation

### Tempo
30-45 minuti

### Success Criteria
- ✅ Tutti gli artifact generati
- ✅ Artifacts sono pronti all'uso
- ✅ So esattamente da dove iniziare
- ✅ Ho checklist completa

### Decisione Post-Fase
**SEI PRONTO PER IMPLEMENTARE!** 🚀

Stato: 🟢 Ready to Implement

Next step: Segui `getting-started.md` negli artifacts

### Note Tecniche
- Artifacts sono guide, non legge
- Puoi deviarli durante implementation
- Mantieni artifacts aggiornati se cambi approccio
- ai-context.md è il file più importante (CLAUDE.md se usi Claude)

---

## Stati e Transizioni

### Stati Disponibili

| Stato | Icon | Significato | Azioni Possibili |
|-------|------|-------------|------------------|
| **Captured** | 🟠 | Idea catturata, non elaborata | ELABORATE, Reject |
| **In Elaboration** | 🟡 | Fase ELABORATE in corso | Complete, Pause |
| **Ready for Validation** | 🔵 | Elaborata, da validare | VALIDATE |
| **To Do** | 🔵 | Validated GO, da documentare | DOCUMENT |
| **Documented** | 🔵 | Documentata, da preparare | PREPARE |
| **Ready to Implement** | 🟢 | Artifacts pronti | START Implementation |
| **In Progress** | 🟡 | Implementation in corso | Continue, Pause |
| **Done** | 🟢 | Implementata e completata | Archive, Iterate |
| **On Hold** | 🔴 | In pausa, review futura | Review, Reject |
| **Rejected** | ⚫ | Scartata | Archive, Learn |

### Diagramma Transizioni

```
                    Nuova Idea
                        ↓
                   🟠 Captured
                    ↙     ↘
            ELABORATE   Reject
                ↓           ↓
          🟡 Elaborating  ⚫ Rejected
                ↓
    🔵 Ready for Validation
                ↓
             VALIDATE
          ↙    ↓    ↘
      NO-GO  LATER  GO
        ↓      ↓      ↓
    ⚫ Rej  🔴 Hold 🔵 To Do
                      ↓
                  DOCUMENT
                      ↓
              🔵 Documented
                      ↓
                  PREPARE
                      ↓
          🟢 Ready to Implement
                      ↓
               IMPLEMENT
                      ↓
            🟡 In Progress
                ↙     ↘
           Complete  Fail
              ↓        ↓
          🟢 Done  🔴 Hold
```

### Regole Transizioni

**Da Captured:**
- → In Elaboration (start ELABORATE)
- → Rejected (scartata senza elaborare)

**Da In Elaboration:**
- → Ready for Validation (ELABORATE completo)
- → On Hold (pausa)
- → Rejected (scartata dopo elaborazione)

**Da Ready for Validation:**
- → To Do (VALIDATE: GO decision)
- → On Hold (VALIDATE: LATER decision)
- → Rejected (VALIDATE: NO-GO decision)

**Da To Do:**
- → Documented (DOCUMENT completo)
- → On Hold (rinviata)

**Da Documented:**
- → Ready to Implement (PREPARE completo)

**Da Ready to Implement:**
- → In Progress (inizio implementation)
- → On Hold (rinviata)

**Da In Progress:**
- → Done (implementation completa)
- → On Hold (bloccata/pausata)
- → Rejected (abbandonata)

**Da On Hold:**
- → Qualsiasi stato precedente (dopo review)
- → Rejected (abbandonata definitivamente)

**Da Done:**
- → Archived (dopo celebrazione!)

---

## File Organization

### Struttura Raccomandata

```
ideas/
├── idea-tracker.md               # Tracker principale
│
├── ideas/                        # Idee individuali
│   ├── idea-001-raw.md
│   ├── idea-001-elaborated.md
│   ├── idea-001-validated.md
│   ├── idea-001-complete.md
│   │
│   ├── idea-002-raw.md
│   └── idea-002-elaborated.md   # Fermata qui
│
├── diagrams/                     # Diagrammi condivisi
│   ├── idea-001-architecture.png
│   └── idea-003-flow.puml
│
├── artifacts/                    # Artifacts per implementation
│   ├── idea-001/
│   │   ├── README.md
│   │   ├── ai-context.md        # CLAUDE.md se usi Claude
│   │   ├── prompts/
│   │   ├── checklists/
│   │   └── templates/
│   │
│   └── idea-004/
│
├── archive/                      # Idee completate/archiviate
│   └── idea-001-done/
│       └── [copia tutti i file]
│
├── prompts/                      # IdeaFlow prompts
│   ├── 01-capture.md
│   ├── 02-elaborate.md
│   ├── 03-validate.md
│   ├── 04-document.md
│   └── 05-prepare.md
│
└── templates/                    # Template custom
    └── my-custom-template.md
```

### Naming Conventions

**Idee:**
- `idea-XXX-raw.md` - Output CAPTURE
- `idea-XXX-elaborated.md` - Output ELABORATE
- `idea-XXX-validated.md` - Output VALIDATE
- `idea-XXX-complete.md` - Output DOCUMENT

**XXX** = numero sequenziale (001, 002, 003...)

**Artifacts:**
- `artifacts/idea-XXX/` - Directory per singola idea
- Contenuto organizzato per tipo (prompts/, checklists/, etc.)

**Archive:**
- Sposta in `archive/` quando idea è Done
- Mantieni struttura completa per reference futura

---

## Best Practices Workflow

### 1. Batch Capture, Sequential Elaborate

```
✅ GOOD:
- Capture 3-5 idee in una sessione
- Elaborate 1 alla volta con focus

❌ BAD:
- Capture 1, elaborate 1, capture 1, elaborate 1 (context switching)
```

### 2. Time-Box Ogni Fase

```
✅ GOOD:
- CAPTURE: 15 min max
- ELABORATE: 45 min max
- VALIDATE: 30 min max
- etc.

❌ BAD:
- Tempo illimitato per fase (analysis paralysis)
```

### 3. Mandatory Pause Capture → Elaborate

```
✅ GOOD:
- Capture oggi
- Elaborate domani (idea "matura")

❌ BAD:
- Capture e immediate elaborate (no time to think)
```

### 4. Review Before Transition

```
✅ GOOD:
Prima di passare a fase successiva, review output:
- È completo?
- Risponde alle domande?
- Sono soddisfatto?

❌ BAD:
- Procedi automaticamente senza review
```

### 5. Update Tracker After Every Phase

```
✅ GOOD:
- Fase completata → update tracker immediately
- Mantieni stato sincronizzato

❌ BAD:
- Update tracker una volta a settimana (info stale)
```

---

## Troubleshooting Workflow

### Problema: "Non riesco a decidere nella fase VALIDATE"

**Causa:** Mancano informazioni per decidere

**Fix:**
1. Torna a ELABORATE
2. Approfondisci aree con dubbi
3. Riprova VALIDATE

### Problema: "ELABORATE produce output troppo generico"

**Causa:** Risposte alle domande troppo superficiali

**Fix:**
1. Rileggi domande AI
2. Rispondi con ESEMPI concreti
3. Spiega il "perché", non solo il "cosa"

### Problema: "DOCUMENT richiede troppo tempo"

**Causa:** Over-documenting

**Fix:**
1. Focus su MVP, non full vision
2. Usa timer (max 2 ore)
3. Documenta essenziale, non perfetto

### Problema: "Artifacts generati non sono utili"

**Causa:** Documentazione incompleta o prompt generici

**Fix:**
1. Review `idea-XXX-complete.md`
2. Assicurati sezione "Architettura" sia dettagliata
3. Specifica stack tecnologico chiaramente
4. Riprova PREPARE con più context

### Problema: "Idea bloccata in In Progress da mesi"

**Causa:** Scope troppo grande o blocco tecnico

**Fix:**
1. Review scope - è troppo ambizioso?
2. Identifica blocker specifico
3. Opzioni:
   - Reduce scope (pivot)
   - On Hold (riprendi dopo)
   - Reject (learn and move on)

---

## Advanced Workflows

### Workflow: Parallel Exploration

Quando hai cluster di idee correlate:

```
Capture idea-A, idea-B, idea-C
    ↓
Elaborate tutte e 3 in parallelo
    ↓
Validate insieme (comparative validation)
    ↓
Scegli la migliore (o combina)
    ↓
Document + Prepare solo quella scelta
```

### Workflow: MVP Iterations

Per progetti iterativi:

```
Idea → ... → DOCUMENT (v1.0 MVP)
    ↓
Implement v1.0
    ↓
Learn from users
    ↓
Capture idea-XXX-v2 (miglioramenti)
    ↓
ELABORATE v2 (skip CAPTURE/VALIDATE, già validato)
    ↓
DOCUMENT v2 → PREPARE v2 → Implement v2
```

### Workflow: Quick Validation Loop

Per testare velocemente molte idee:

```
Batch CAPTURE (10 idee)
    ↓
Quick ELABORATE (20 min each)
    ↓
Quick VALIDATE (10 min each)
    ↓
Keep top 2-3 GO
    ↓
Full DOCUMENT + PREPARE solo quelle
```

---

**Il workflow è flessibile. Adattalo al tuo stile di lavoro!**
