# 🌊 IdeaFlow

> Framework open-source per catturare, elaborare e documentare idee usando l'AI come partner intelligente.

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![GitHub stars](https://img.shields.io/github/stars/disoardi/ideaflow)](https://github.com/disoardi/ideaflow/stargazers)

## 🎯 Cos'è IdeaFlow?

IdeaFlow è un **framework** (non un tool) che ti guida nel processo di gestione idee con l'aiuto dell'AI. Fornisce:

- 📝 **Template strutturati** per catturare e organizzare idee
- 🤖 **Prompt pattern** ottimizzati per ogni fase del processo
- 📊 **Sistema di tracking** con stati chiari e visuali
- 🔄 **Workflow in 5 fasi** dal pensiero grezzo all'implementazione
- 🌍 **AI-agnostic** - funziona con Claude, ChatGPT, Gemini, qualsiasi LLM

## 💡 Perché IdeaFlow?

Quante volte hai avuto un'idea brillante che poi hai dimenticato? O hai iniziato a implementare qualcosa senza pensarci abbastanza?

IdeaFlow risolve questo problema fornendo un **processo sistematico** supportato dall'AI per:

- ✅ **Mai perdere un'idea** - cattura tutto, anche pensieri grezzi
- ✅ **Elaborare sistematicamente** - l'AI ti guida con domande mirate
- ✅ **Decidere consapevolmente** - valida prima di investire tempo
- ✅ **Documentare completamente** - crea documentazione dettagliata
- ✅ **Partire preparato** - genera materiali pronti per implementazione

## 🔄 Processo in 5 Fasi

```
CAPTURE → ELABORATE → VALIDATE → DOCUMENT → PREPARE
  ↓          ↓           ↓           ↓          ↓
Grezza   Approfondita  Decisione  Completa   Ready to
                                               Implement
```

## 🚀 Quick Start

### 1. Scarica il Framework

```bash
git clone https://github.com/disoardi/ideaflow.git
cd ideaflow
```

### 2. Copia i Template

```bash
# Crea la tua directory idee
mkdir my-ideas
cp templates/core/idea-tracker.md my-ideas/
cp -r templates/prompts my-ideas/
```

### 3. Cattura la Tua Prima Idea

Apri `my-ideas/prompts/01-capture.md`, copia il prompt e usalo con il tuo AI preferito.

### 4. Segui il Workflow

Usa i prompt delle 5 fasi in sequenza per elaborare la tua idea.

📖 **Leggi la [Guida Completa](docs/getting-started.md) per il tutorial dettagliato.**

## 📖 Documentazione

- [Getting Started](docs/getting-started.md) - Tutorial passo-passo
- [Workflow Guide](docs/workflow-guide.md) - Guida alle 5 fasi
- [Best Practices](docs/best-practices.md) - Consigli efficaci
- [Customization](docs/customization.md) - Personalizzazione
- [FAQ](docs/faq.md) - Domande frequenti

## 💼 Casi d'Uso

- 💻 **Progetti Software** - Dall'idea al codice strutturato
- 🎨 **Progetti Creativi** - Organizza idee creative
- 📚 **Apprendimento** - Traccia obiettivi studio
- 🚀 **Startup Ideas** - Valida idee business
- 🔬 **Research** - Organizza ricerche
- 🛠️ **Hobby Projects** - Gestisci progetti personali

## 🤝 Come Contribuire

IdeaFlow è un progetto community-driven. Contribuzioni benvenute!

### Workflow Git-Based

#### 1. Fork del Repository

Vai su https://github.com/disoardi/ideaflow e clicca "Fork"

#### 2. Clone del Tuo Fork

```bash
# Clone il TUO fork (non il repo principale)
git clone https://github.com/TUO-USERNAME/ideaflow.git
cd ideaflow

# Aggiungi upstream per sync futuro
git remote add upstream https://github.com/disoardi/ideaflow.git
```

#### 3. Crea Branch per la Tua Modifica

```bash
# Crea e switch a nuovo branch
git checkout -b feature/nome-tua-feature

# Esempi di nomi branch:
# - feature/new-business-template
# - docs/improve-getting-started
# - fix/typo-in-readme
```

#### 4. Fai le Tue Modifiche

Modifica/aggiungi file nel tuo branch:
- Nuovi template in `templates/`
- Miglioramenti docs in `docs/`
- Nuovi esempi in `examples/`
- etc.

#### 5. Commit sul Tuo Repository

```bash
# Aggiungi file modificati
git add .

# Commit con messaggio descrittivo
git commit -m "✨ Add business plan template"

# Push sul TUO fork
git push origin feature/nome-tua-feature
```

#### 6. Apri Pull Request

1. Vai sul TUO fork su GitHub
2. Vedrai banner "Compare & pull request" - clicca
3. Compila:
   - **Base repository:** disoardi/ideaflow (main)
   - **Head repository:** TUO-USERNAME/ideaflow (tuo branch)
   - **Titolo:** Descrittivo e chiaro
   - **Descrizione:** Spiega cosa hai aggiunto/modificato e perché
4. Click "Create pull request"

#### 7. Review e Merge

- Maintainer reviewerà la PR (entro 7 giorni)
- Eventuali richieste di modifica
- Quando approvata: merge nel repo principale
- Il tuo contributo sarà nella prossima release!

### Mantenere il Fork Aggiornato

```bash
# Periodicamente, sincronizza con upstream
git checkout main
git fetch upstream
git merge upstream/main
git push origin main
```

### 💡 Cosa Contribuire

- **Template:** Nuovi template per use case specifici
- **Prompt:** Ottimizzazioni prompt per AI specifici
- **Docs:** Miglioramenti documentazione, correzioni, traduzioni
- **Esempi:** Workflow reali (anonimizzati)
- **Bug Fix:** Correzioni errori

Vedi [CONTRIBUTING.md](CONTRIBUTING.md) per dettagli completi.

## 📜 Licenza

GPL-3.0 - Vedi [LICENSE](LICENSE)

## 💬 Community

- [Discussions](https://github.com/disoardi/ideaflow/discussions) - Domande e feedback
- [Issues](https://github.com/disoardi/ideaflow/issues) - Bug e feature request
- [Showcase](https://github.com/disoardi/ideaflow/discussions/categories/showcase) - Condividi i tuoi progetti

---

**Made with 🧠 and 🤖 by [disoardi](https://github.com/disoardi)**

*"Never lose an idea again. Let AI help you turn thoughts into reality."*
