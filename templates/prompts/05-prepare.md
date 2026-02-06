# 🚀 Prompt Fase 5: PREPARE (Prepara Implementazione)

> Usa questo prompt per generare materiali concreti pronti per iniziare l'implementazione.

---

## 📋 Istruzioni

1. Completa tutte le fasi precedenti
2. Assicurati di avere documentazione completa (`idea-XXX-complete.md`)
3. Copia il prompt sotto
4. Allega la documentazione completa
5. Salva gli output nella directory `artifacts/idea-XXX/`

---

## 💬 PROMPT

Ho questa idea completamente documentata e voglio generare materiali per iniziare l'implementazione:

[INCOLLA QUI IL CONTENUTO COMPLETO DEL FILE idea-XXX-complete.md]

**Genera per me i seguenti materiali pronti all'uso:**

---

## 🎯 Materiali da Generare

### 1. 📄 ai-context.md (Context File per AI Coding Assistant)

Crea file `ai-context.md` completo che includa:

**Header:**
```markdown
# [Nome Progetto] - AI Context

> Context completo per sviluppo progetto con AI
```

**Sezioni:**
- **Project Overview**: Descrizione breve e chiara
- **Goals**: Obiettivi misurabili
- **Architecture**: Architettura high-level
- **Tech Stack**: Tecnologie e perché
- **Key Requirements**: Requisiti principali (max 10)
- **Development Principles**: Principi guida sviluppo
- **Code Style**: Convenzioni codice
- **Testing Strategy**: Approccio testing
- **Deployment**: Note su deploy
- **Important Context**: Qualsiasi altra info critica

**Formato:** Markdown completo, ready to use con AI coding assistant

> **💡 Note per diversi LLM:**
> - **Claude Code/Projects**: Rinomina in `CLAUDE.md` per context automatico
> - **ChatGPT/GPT-4**: Carica all'inizio della sessione o usa Custom Instructions
> - **Cursor/Windsurf**: Aggiungi alle `.cursorrules` o project instructions
> - **Copilot/GitHub**: Usa come doc di riferimento nel workspace
> - **Altri AI IDE**: Consulta la doc per integrare il context file

### 2. 🎯 Setup Prompts (serie di prompt per implementazione)

Crea sequenza di prompt per guidare sviluppo fase per fase:

**Prompt 1: Project Initialization**
```markdown
# Prompt: Inizializzazione Progetto

Basandoti sul context in ai-context.md, genera:
1. Struttura directory completa del progetto
2. File di configurazione base necessari
3. README.md con setup instructions
4. .gitignore appropriato

[Dettagli specifici del progetto]
```

**Prompt 2-N: Implementation Phases**
Un prompt per ogni fase principale:
- Setup ambiente
- Core functionality
- Testing
- Documentation
- Deploy

Ogni prompt deve:
- Essere self-contained
- Riferirsi a ai-context.md per context
- Specificare output atteso
- Includere acceptance criteria

### 3. 📁 Repository Structure

Genera struttura completa directory del progetto:

```
project-name/
├── README.md
├── LICENSE
├── .gitignore
├── [altri file config specifici]
├── src/
├── tests/
├── docs/
└── [altre directory]
```

Per ogni directory, spiega:
- Cosa contiene
- Perché esiste
- Convenzioni da seguire

### 4. 📋 Implementation Checklist

Crea checklist dettagliata per implementazione:

**Phase 1: Setup** (Giorni 1-X)
- [ ] Task 1 specifico
  - Subtask 1.1
  - Subtask 1.2
- [ ] Task 2 specifico
- **Checkpoint**: [Criterio successo]

**Phase 2: Core Development** (Giorni X-Y)
- [ ] Feature 1
  - [ ] Subtask
- [ ] Feature 2
- **Milestone**: [Criterio successo]

[...continua per tutte le fasi]

**Acceptance Criteria** per ogni fase:
- [Criterio 1]
- [Criterio 2]

### 5. 🧪 Testing Plan

Genera piano di testing:

**Unit Tests:**
- Cosa testare
- Tool da usare
- Coverage target

**Integration Tests:**
- Scenari da testare
- Setup necessario

**End-to-End Tests:**
- User scenarios
- Validation criteria

**Test Template:**
```
# Test: [Nome]
## Setup
[Come preparare test]
## Execution
[Step by step]
## Expected Result
[Cosa dovrebbe succedere]
## Acceptance
[Quando considerato passed]
```

### 6. 📚 Getting Started Guide

Crea guida per iniziare implementazione:

```markdown
# Getting Started - [Nome Progetto]

## Prerequisites
[Lista prerequisiti]

## Setup
1. [Primo step]
2. [Secondo step]

## Your First Task
[Cosa fare per primo]

## Next Steps
[Cosa fare dopo]

## Need Help?
[Dove trovare info]
```

### 7. 📊 Progress Tracker Template

Template per tracciare progresso:

```markdown
# Progress Tracker - [Nome Progetto]

## Current Status
**Phase:** [Nome fase]
**Progress:** XX%
**Blockers:** [Se presenti]

## Completed
- [x] Task 1
- [x] Task 2

## In Progress
- [ ] Task 3

## Todo
- [ ] Task 4

## Notes
[Note di progresso]
```

### 8. 🔧 Configuration Templates

Genera template configurazione necessari:

**Per progetti software:**
- `package.json` / `requirements.txt` / `go.mod` (secondo stack)
- Config file framework usati
- `.env.example` con variabili necessarie
- CI/CD config base

**Per altri progetti:**
- Config file appropriati per tipo progetto

### 9. 📖 Documentation Templates

Template per documentazione:

**API Documentation** (se applicabile):
```markdown
# API Documentation

## Endpoint: [Nome]
**Method:** GET/POST/...
**URL:** /api/v1/...
**Description:** [Cosa fa]
**Parameters:** [Lista]
**Response:** [Formato]
**Example:**
[Esempio request/response]
```

**User Guide Template:**
```markdown
# User Guide - [Feature]

## Overview
[Cosa fa]

## How to Use
[Step by step]

## Examples
[Esempi pratici]

## Troubleshooting
[Problemi comuni]
```

### 10. 🎬 Quick Start Script

Se appropriato, genera script di quick start:

```bash
#!/bin/bash
# Quick start script per [Nome Progetto]

echo "🚀 Starting [Nome Progetto] setup..."

# Step 1: Check prerequisites
# Step 2: Install dependencies
# Step 3: Setup configuration
# Step 4: Run initial setup
# ...

echo "✅ Setup complete! Ready to start."
```

---

## 📦 Output Organization

Organizza tutti i file generati in questa struttura:

```
artifacts/idea-XXX/
├── README.md                          # Indice di tutti gli artifact
├── ai-context.md                          # Context per Claude Code
├── prompts/
│   ├── 01-init-project.md
│   ├── 02-core-development.md
│   ├── 03-testing.md
│   └── 04-deployment.md
├── structure/
│   ├── directory-tree.md              # Struttura directory completa
│   └── file-descriptions.md           # Descrizione ogni file
├── checklists/
│   ├── implementation-checklist.md
│   ├── testing-checklist.md
│   └── deployment-checklist.md
├── templates/
│   ├── config-templates/
│   ├── documentation-templates/
│   └── test-templates/
├── guides/
│   ├── getting-started.md
│   └── troubleshooting.md
└── scripts/
    └── quick-start.sh (se applicabile)
```

---

## ✅ Checklist Completezza Artifacts

Verifica che siano stati generati:

- [ ] ai-context.md completo e dettagliato
- [ ] Prompt sequence per implementazione (minimo 3-5 prompt)
- [ ] Struttura repository con spiegazioni
- [ ] Implementation checklist dettagliata
- [ ] Testing plan completo
- [ ] Getting started guide
- [ ] Progress tracker template
- [ ] Configuration templates necessari
- [ ] Documentation templates
- [ ] Scripts utility (se applicabili)
- [ ] README.md che spiega come usare tutti gli artifact

---

## 📝 Dopo il Prompt

1. ✅ Salva tutti i file generati in `artifacts/idea-XXX/`
2. ✅ Crea file `artifacts/idea-XXX/README.md` con indice e istruzioni
3. ✅ Aggiorna stato tracker: 🔵 Documented → 🟢 Ready to Implement
4. ✅ Review artifacts per completezza
5. ✅ **SEI PRONTO PER INIZIARE!** 🚀
6. ✅ Primo step: Leggi `getting-started.md` e inizia implementation

---

## 🎉 Next: Implementation!

Ora hai tutto ciò che serve per iniziare:
- Context completo per AI (ai-context.md)
- Prompt per ogni fase
- Checklist per non perdere nulla
- Template pronti all'uso

**Inizia dal prompt 01-init-project.md e segui la sequenza!**

Good luck! 💪

---

*Prompt da IdeaFlow Framework - https://github.com/disoardi/ideaflow*
