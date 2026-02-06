# ❓ FAQ - IdeaFlow

Domande frequenti su IdeaFlow.

## Generale

### Q: Cos'è IdeaFlow?
**A:** IdeaFlow è un framework (non un tool) per catturare, elaborare e documentare idee usando l'AI come partner intelligente. Fornisce template, prompt e workflow strutturato per non perdere mai un'idea e portarla dall'intuizione all'implementazione.

### Q: IdeaFlow è gratis?
**A:** Sì, IdeaFlow è open-source con licenza GPL-3.0. È completamente gratuito.

### Q: Serve un AI specifico?
**A:** No! IdeaFlow è AI-agnostic. Funziona con Claude, ChatGPT, Gemini, Llama, o qualsiasi LLM. I prompt sono generici e adattabili.

### Q: Serve saper programmare?
**A:** No! IdeaFlow è un framework basato su markdown e prompt. Non richiede coding. È perfetto per chiunque: sviluppatori, creativi, ricercatori, business people, etc.

---

## Getting Started

### Q: Da dove inizio?
**A:** Leggi [Getting Started Guide](getting-started.md). In sintesi:
1. Clone repository
2. Copia template
3. Cattura prima idea usando prompt 01-capture.md
4. Segui il workflow

### Q: Quanto tempo serve per imparare?
**A:** 30-60 minuti per capire le basi. Dopo 2-3 idee sarai fluent nel workflow.

### Q: Posso usare solo alcune fasi?
**A:** Sì! Non tutte le idee richiedono tutte le 5 fasi. Puoi:
- Catturare e basta (stato Captured)
- Fermarti dopo Validate
- Fare workflow custom (vedi [Customization](customization.md))

### Q: Dove salvo i miei file?
**A:** Dove preferisci! Opzioni:
- Directory locale `~/ideas`
- Obsidian vault
- Notion workspace
- GitHub private repository
- Silverbullet
- Qualsiasi sistema supporti markdown

---

## Workflow

### Q: Devo seguire le fasi in ordine?
**A:** Sì, l'ordine è pensato per essere ottimale. Ma puoi:
- Saltare fasi per idee semplici
- Tornare indietro se serve
- Creare workflow custom (vedi FAQ "Posso personalizzare")

### Q: Quanto tempo richiedono le fasi?
**A:**
- CAPTURE: 10-15 min
- ELABORATE: 30-45 min
- VALIDATE: 20-30 min
- DOCUMENT: 1-2 hours
- PREPARE: 30-45 min

**Totale MVP:** ~3-4 hours per idea completa

### Q: Cosa faccio se mi blocco in una fase?
**A:** 
1. Review output fase precedente
2. Fai break, torna dopo
3. Chiedi all'AI domande diverse
4. Skip fase e vai avanti (puoi sempre tornare)
5. Chiedi aiuto nella [Community](https://github.com/disoardi/ideaflow/discussions)

### Q: Posso usare AI diversi per fasi diverse?
**A:** Sì! Strategia multi-AI è valida:
- CAPTURE: ChatGPT (veloce)
- ELABORATE: Claude (profondo)
- VALIDATE: Gemini (prospettiva diversa)

### Q: Come decido quando fermarmi?
**A:**
- CAPTURE: Sempre (costa poco, beneficio alto)
- ELABORATE: Solo se idea promettente
- VALIDATE: Se hai dubbio su fattibilità
- DOCUMENT: Solo se decisione è GO
- PREPARE: Sempre prima di implementare

---

## Prompts

### Q: I prompt non funzionano bene con il mio AI
**A:** I prompt sono generici. Adattali:
1. Copia prompt in `prompts/my-prompts/`
2. Modifica per il tuo AI
3. Testa con 2-3 idee
4. Itera fino a ottimizzazione

### Q: Posso scrivere prompt in lingua diversa?
**A:** Sì! Traduci prompt nella tua lingua. Framework funziona in qualsiasi lingua.

### Q: L'AI mi dà risposte troppo generiche
**A:** 
- Sii più specifico nelle risposte
- Fornisci esempi concreti
- Usa follow-up: "Puoi essere più specifico su X?"
- Allega context aggiuntivo

### Q: Posso modificare prompt esistenti?
**A:** Sì! Anzi, è incoraggiato. Vedi [Customization Guide](customization.md).

---

## Template

### Q: Devo usare template forniti?
**A:** No, sono un starting point. Puoi:
- Usarli as-is
- Modificarli
- Crearne di nuovi
- Combinare sezioni diverse

### Q: Come creo template custom?
**A:** Vedi [Customization Guide](customization.md) sezione "Custom Templates".

### Q: Posso condividere i miei template?
**A:** Sì! Apri PR o Discussion. Community apprecia contributi.

---

## Stati

### Q: Cosa significano gli stati?
**A:** Vedi [Workflow Guide](workflow-guide.md) sezione "Stati e Transizioni".

Quick:
- 🟠 Captured = Catturata
- 🟡 In Progress = In lavorazione
- 🔵 To Do = Pronta per iniziare
- 🟢 Done = Completata
- 🔴 On Hold = In pausa
- ⚫ Rejected = Scartata

### Q: Posso aggiungere stati custom?
**A:** Sì! Vedi [Customization Guide](customization.md) sezione "Stati Custom".

### Q: Come cambio stato idea?
**A:** Manualmente nel tracker. Update tabella e dettaglio idea.

### Q: Quante idee posso avere per stato?
**A:** Nessun limite, ma raccomandazioni:
- Captured: max 10 (elabora prima di aggiungere altre)
- In Progress: max 3 (focus!)
- To Do: quante vuoi

---

## Tools & Integration

### Q: C'è una app per IdeaFlow?
**A:** No, IdeaFlow è un framework markdown-based. Ma puoi usarlo con:
- Obsidian (raccomandato)
- Notion
- VS Code
- Silverbullet
- Qualsiasi editor markdown

### Q: Funziona con Obsidian?
**A:** Perfettamente! Usa dataview per query dinamiche.

### Q: C'è CLI tool?
**A:** In roadmap. Per ora, framework è file-based.

### Q: Posso automatizzare parti del workflow?
**A:** Sì! Script custom, GitHub Actions, etc. Vedi [Customization Guide](customization.md).

---

## Community & Support

### Q: Dove chiedo aiuto?
**A:**
- [GitHub Discussions](https://github.com/disoardi/ideaflow/discussions)
- [GitHub Issues](https://github.com/disoardi/ideaflow/issues) per bug
- Community channel (coming soon)

### Q: Come contribuisco?
**A:** Leggi [CONTRIBUTING.md](../CONTRIBUTING.md). Puoi:
- Nuovi template
- Prompt ottimizzati
- Esempi workflow
- Fix documentazione
- Traduzioni

### Q: Posso condividere le mie idee?
**A:** Sì! Usa [Showcase Discussion](https://github.com/disoardi/ideaflow/discussions/categories/showcase).

**IMPORTANTE:** Anonimizza informazioni sensibili.

---

## Use Cases

### Q: Per cosa posso usare IdeaFlow?
**A:** Qualsiasi tipo di idea:
- Progetti software
- Startup ideas
- Creative projects
- Learning goals
- Research topics
- Content creation
- Personal projects
- Business strategies

### Q: È solo per progetti tech?
**A:** No! Template tech sono esempi, ma framework è generico. Vedi [Customization Guide](customization.md) per template non-tech.

### Q: Funziona per team?
**A:** Sì, ma è pensato principalmente per uso individuale. Per team:
- Repository condiviso
- Review process
- Collaborative validation
- Vedi [Workflow Guide](workflow-guide.md) "Collaborative Workflow"

---

## Best Practices

### Q: Quante idee dovrei catturare?
**A:** Cattura TUTTE. Filtra in fase VALIDATE. Non auto-censurarti in fase CAPTURE.

### Q: Quando revieware idee?
**A:** 
- **Weekly:** Quick review stati
- **Monthly:** Deep review + cleanup
- Vedi [Best Practices](best-practices.md)

### Q: Devo documentare idee rejected?
**A:** Sì! Documenta WHY rejected. Learnings sono preziosi.

### Q: È normale avere molte idee rejected?
**A:** Sì! Success rate tipico: ~2-5% idee catturate diventano successi. È normale e sano.

---

## Troubleshooting

### Q: Non riesco a decidere in fase VALIDATE
**A:**
1. Torna a ELABORATE
2. Approfondisci dubbi
3. Chiedi feedback esterno
4. OK dire "On Hold, decido dopo"

### Q: ELABORATE produce output troppo lungo
**A:** 
- Riduci verbosity nelle risposte
- Chiedi all'AI di essere conciso
- Focus su essenziale

### Q: Non trovo tempo per DOCUMENT
**A:**
- Blocca 2 ore dedicate
- Usa timer (Pomodoro)
- OK fare mini-documentation per MVP

### Q: Troppi artifact in PREPARE
**A:**
- Genera solo artifact che userai
- Skip quelli non rilevanti per il tuo stack
- Focus su essenziale (claude.md + checklist)

---

## Advanced

### Q: Posso fare workflow custom?
**A:** Assolutamente! Vedi [Customization Guide](customization.md). Framework è flessibile.

### Q: Come misuro efficacia del framework?
**A:** Traccia metriche:
- Conversion rate (capture → done)
- Time per fase
- Success rate implementation
- Vedi [Best Practices](best-practices.md) "Metriche"

### Q: Posso contribuire al framework?
**A:** Sì! 
- Template custom
- Prompt ottimizzati
- Esempi workflow
- Fix docs
- Vedi [CONTRIBUTING.md](../CONTRIBUTING.md)

---

## Technical

### Q: Quali file genera IdeaFlow?
**A:**
- `idea-XXX-raw.md` (CAPTURE)
- `idea-XXX-elaborated.md` (ELABORATE)
- `idea-XXX-validated.md` (VALIDATE)
- `idea-XXX-complete.md` (DOCUMENT)
- `artifacts/idea-XXX/` (PREPARE)

### Q: Posso usare IdeaFlow offline?
**A:** Sì per template e file. No per prompt con AI (serve connessione).

### Q: Come backup le mie idee?
**A:**
- Git repository (raccomandato)
- Cloud storage (Dropbox, Drive)
- Regular export
- Vedi [Getting Started](getting-started.md)

---

## Licensing

### Q: Posso usare IdeaFlow commercialmente?
**A:** Sì! GPL-3.0 permette uso commerciale.

### Q: Posso modificare IdeaFlow?
**A:** Sì! GPL-3.0 permette modifiche. Se distribuisci versione modificata, deve essere GPL-3.0.

### Q: Devo citare IdeaFlow?
**A:** Non obbligatorio, ma appreciated! 🙏

---

## Feedback

### Q: Come fornire feedback?
**A:** 
- [GitHub Discussions](https://github.com/disoardi/ideaflow/discussions)
- [GitHub Issues](https://github.com/disoardi/ideaflow/issues)
- Direct contact (in README)

### Q: Feature requests?
**A:** Apri [Feature Request Issue](https://github.com/disoardi/ideaflow/issues/new?template=feature-request.md)

---

## 🆘 Non trovi risposta?

**Ask the community:**
[GitHub Discussions](https://github.com/disoardi/ideaflow/discussions)

**Found a bug:**
[Open Issue](https://github.com/disoardi/ideaflow/issues)

**Want to contribute:**
[Contributing Guidelines](../CONTRIBUTING.md)

---

*FAQ aggiornate continuamente. Contribuisci con tue domande!*