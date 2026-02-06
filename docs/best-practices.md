# 📖 IdeaFlow Best Practices

Pratiche consigliate basate sull'esperienza di utilizzo del framework.

## 🎯 Principi Fondamentali

### 1. Cattura Sempre, Filtra Dopo

**Problema:** "Non catturo idee perché penso non siano abbastanza buone"

**Best Practice:**
- ✅ Cattura QUALSIASI idea, anche se sembra banale
- ✅ La fase VALIDATE serve proprio a filtrare
- ✅ Costa poco catturare, costa molto dimenticare un'idea buona

**Esempio:**
Un'idea che sembra banale oggi potrebbe connettersi con un'altra idea domani e diventare brillante.

### 2. Elabora con Calma

**Problema:** "Catturo e poi elaboro subito di fretta"

**Best Practice:**
- ✅ Lascia "maturare" l'idea almeno qualche ora
- ✅ Blocca tempo dedicato per elaborazione (30-45 min senza interruzioni)
- ✅ Rispondi onestamente alle domande, non quello che l'AI vuole sentire

**Esempio:**
```
Catturo idea alle 10:00
↓
Lascio riposare fino al pomeriggio
↓
Elaboro alle 15:00 quando sono fresco e concentrato
```

### 3. Valida Senza Pietà

**Problema:** "Valido tutte le idee come GO perché mi piacciono"

**Best Practice:**
- ✅ Sii critico e realistico nella validazione
- ✅ OK dire NO a un'idea che ami ma non è fattibile ORA
- ✅ On Hold è una scelta valida
- ✅ Rejected non significa "idea cattiva", significa "non ora/non per me"

**Red Flags:**
- "Farò quando avrò tempo" (non lo avrai mai)
- "È facile" (se fosse facile l'avresti già fatto)
- "Tutti ne hanno bisogno" (validare assumption!)

### 4. Documenta Prima, Implementa Poi

**Problema:** "Inizio a implementare senza documentare"

**Best Practice:**
- ✅ Se hai deciso GO, documenta completamente
- ✅ La documentazione è la tua mappa durante implementation
- ✅ Tempo speso in documentazione si recupera in implementation

**ROI Documentazione:**
```
1 ora documentazione = Risparmio 3-5 ore di implementation confusa
```

### 5. Usa gli Artifacts

**Problema:** "Inizio implementazione senza preparare artifacts"

**Best Practice:**
- ✅ Genera sempre artifacts prima di implementare
- ✅ Usa claude.md per mantenere context con AI
- ✅ Segui la checklist, non andare a memoria

---

## 🔄 Workflow Patterns

### Pattern 1: Quick Validation

**Scenario:** Vuoi validare velocemente molte idee.

**Workflow:**
1. Capture batch (5-10 idee in una sessione)
2. Elaborate solo le top 3 più promettenti
3. Validate solo quelle elaborate
4. Document solo quella che passa validate

**Quando usarlo:** Brainstorming sessions, idea generation sprints

### Pattern 2: Deep Dive

**Scenario:** Hai un'idea specifica che vuoi esplorare a fondo.

**Workflow:**
1. Capture idea principale
2. Durante elaborate, cattura sotto-idee che emergono
3. Crea collegamenti tra idea principale e sotto-idee
4. Validate cluster di idee insieme
5. Document soluzione completa

**Quando usarlo:** Progetti complessi, startup ideas, research topics

### Pattern 3: Iterative Refinement

**Scenario:** Un'idea che evolve nel tempo.

**Workflow:**
1. Capture versione 1.0
2. Elaborate → Validate → Rejected/On Hold
3. Dopo qualche settimana/mese, nuovi input
4. Capture versione 2.0 (con link a v1)
5. Elaborate v2 → Validate → potrebbe essere GO ora

**Quando usarlo:** Idee ambiziose, long-term vision

---

## 📊 Gestione Tracker

### Revisione Settimanale

**Ogni settimana (15-20 minuti):**

```markdown
## Weekly Review Checklist

- [ ] Review idee 🟠 Captured da >7 giorni
  - Decisione: elaborare o scartare
  
- [ ] Review idee 🔴 On Hold
  - È tempo di revisitare?
  
- [ ] Review idee 🟡 In Progress
  - Ci sono blocchi?
  - Servono pivoting?
  
- [ ] Update statistiche tracker

- [ ] Identifica pattern
  - Quali categorie dominate?
  - Dove investo più tempo?
```

### Revisione Mensile

**Ogni mese (30-45 minuti):**

```markdown
## Monthly Review Checklist

- [ ] Analisi metriche
  - Quante idee catturate?
  - Quante validate GO?
  - Quante implemented?
  - Conversion rate capture → done?
  
- [ ] Review collegamenti
  - Idee correlate da connettere?
  - Cluster di idee da unificare?
  
- [ ] Cleanup
  - Idee ⚫ Rejected da archiviare?
  - File vecchi da organizzare?
  
- [ ] Retrospettiva
  - Cosa ho imparato?
  - Quali best practice personali?
```

### Stati e Transizioni

**Regole per cambi stato:**

```
🟠 Captured
  ↓ dopo ELABORATE
🟡 In Elaboration
  ↓ dopo review elaborazione
🔵 Ready for Validation
  ↓ dopo VALIDATE
├→ ⚫ Rejected (documenta perché)
├→ 🔴 On Hold (setta data review)
└→ 🔵 To Do
      ↓ dopo DOCUMENT
  🔵 Documented
      ↓ dopo PREPARE
  🟢 Ready to Implement
      ↓ durante implementation
  🟡 In Progress
      ↓ dopo completamento
  🟢 Done
```

---

## 💡 Tips Avanzati

### Tip 1: Template Personalizzati

Crea template custom per domini specifici:

```
templates/
├── my-templates/
    ├── saas-idea.md
    ├── research-paper.md
    └── learning-project.md
```

Ogni template può avere sezioni specifiche per quel dominio.

### Tip 2: Tag System

Usa tag nel tracker per categorizzare meglio:

```markdown
## 🏷️ Tag

`#tech` `#ai` `#tool` `#quick-win` `#high-impact`
```

Poi filtra con search: cerchi `#quick-win` trovi tutte le quick wins.

### Tip 3: Collegamenti Espliciti

Quando trovi connessioni tra idee, sii esplicito:

```markdown
### Idea #005: Tool X

**🔗 Collegamenti:**
- [Idea #002]: Questa idea potrebbe usare template da #002
- [Idea #003]: Risultati di #003 potrebbero alimentare #005
```

### Tip 4: Versioning

Per idee che evolvono molto:

```
ideas/
├── idea-001-v1-rejected.md
├── idea-001-v2-onhold.md
└── idea-001-v3-current.md
```

Nel tracker, link alla versione current.

### Tip 5: Mini-Artifacts

Per idee validate ma non ancora documented, crea mini-artifacts:

```
artifacts/idea-XXX-quick/
├── one-pager.md          # Executive summary
├── next-steps.md         # Immediate actions
└── resources.md          # Links & resources
```

Utile per condividere velocemente l'idea con altri.

---

## 🚫 Anti-Patterns

### Anti-Pattern 1: "Idea Hoarding"

**Sintomo:** 50+ idee captured, 0 elaborate.

**Problema:** Catturi ma non processi.

**Fix:**
- Regola: Max 10 idee in stato Captured
- Se arrivi a 10, DEVI elaborare/scartare prima di catturare altre

### Anti-Pattern 2: "Validation Bias"

**Sintomo:** Validate sempre GO per idee che ti piacciono.

**Problema:** Confirmation bias, non sei obiettivo.

**Fix:**
- Chiedi a qualcuno di leggere la validate e darti feedback
- Usa punteggi numerici oggettivi
- Red team: chiedi all'AI di farti domande critiche

### Anti-Pattern 3: "Analysis Paralysis"

**Sintomo:** 5 ore di documentation per idea semplice.

**Problema:** Over-engineering nella fase doc.

**Fix:**
- Timer: max 2 ore per document
- Focus su essenziale, non perfetto
- Puoi sempre iterare dopo

### Anti-Pattern 4: "Scope Creep"

**Sintomo:** Idea inizia semplice, diventa mostro.

**Problema:** Non definisci scope chiaro in validate.

**Fix:**
- In validate, definisci esplicitamente MVP scope
- Crea idea separata per "Version 2.0"
- Document solo MVP, non full vision

### Anti-Pattern 5: "Ghost Ideas"

**Sintomo:** Idee in stato In Progress da mesi.

**Problema:** Non riesci a procedere ma non vuoi ammettere fallimento.

**Fix:**
- Review mensile obbligatoria
- Se stuck da >1 mese → On Hold o Rejected
- OK fallire, documenta learnings e vai avanti

---

## 📈 Metriche Utili

Traccia queste metriche per migliorare il tuo processo:

### Funnel Metrics

```
Captured: 20 idee
  ↓
Elaborated: 12 idee (60% conversion)
  ↓
Validated GO: 5 idee (42% conversion)
  ↓
Documented: 4 idee (80% conversion)
  ↓
Implemented: 2 idee (50% conversion)
  ↓
Done & Successful: 1 idea (50% success rate)
```

### Time Metrics

```
Tempo medio per fase:
- Capture: 12 min
- Elaborate: 38 min
- Validate: 25 min
- Document: 1.5 hours
- Prepare: 35 min

Time to implement (da capture a done): 6 settimane
```

### Quality Metrics

```
% idee che arrivano a Done: 5% (1 su 20)
% idee Done che sono successi: 50%

→ Success rate finale: 2.5% di idee catturate diventano successi
```

**Questo è normale!** Non tutte le idee devono essere successi.

---

## 🎓 Learnings dalla Community

*Questa sezione sarà popolata con learnings dalla community man mano che il framework viene usato.*

### Learning 1: [TBD]
*Contribuisci i tuoi learnings!*

---

## 🤝 Contributing

Hai best practices da condividere?

1. Usale per almeno 3-4 idee
2. Documenta risultati
3. Proponi PR o apri Discussion

Le best practices della community saranno integrate in questo documento.

---

**Remember: Il framework è una guida, non una prigione. Adattalo alle tue esigenze!**
