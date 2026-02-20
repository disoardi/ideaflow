---
layout: default
title: IdeaFlow
description: Dal pensiero grezzo all'implementazione, con l'AI che ti guida
---

# IdeaFlow

**Hai un'idea? Questo framework ti guida dall'idea grezza all'implementazione.**

Funziona con qualsiasi AI: Claude, ChatGPT, Gemini, o qualsiasi LLM.

---

## Come funziona

IdeaFlow è un insieme di **template e prompt** (non software da installare). Copi un prompt, lo dai all'AI, e lei ti guida con domande strutturate.

Il processo è diviso in **5 fasi**:

| Fase | Cosa fai | Tempo |
|------|----------|-------|
| **1. CAPTURE** | Catturi l'idea grezza prima che sparisca | 10-15 min |
| **2. ELABORATE** | L'AI ti pone domande per approfondire | 30-45 min |
| **3. VALIDATE** | Decidi: vale la pena? GO / NO-GO | 20-30 min |
| **4. DOCUMENT** | Crei documentazione completa | 1-2 ore |
| **5. PREPARE** | Generi materiali pronti per iniziare | 30-45 min |

---

## Inizia in 3 passi

**Passo 1 — Scarica il framework**
```bash
git clone https://github.com/disoardi/ideaflow.git
cd ideaflow
```

**Passo 2 — Copia i prompt nella tua cartella**
```bash
mkdir mie-idee
cp templates/core/idea-tracker.md mie-idee/
cp -r templates/prompts mie-idee/
```

**Passo 3 — Cattura la prima idea**

Apri `mie-idee/prompts/01-capture.md`, copia il prompt e incollalo nel tuo AI preferito.

---

## Usa Claude per iniziare subito

Hai Claude Code? Puoi partire senza installare nulla:

1. Apri Claude Code
2. Incolla questo messaggio:

```
Leggi il file AI.md in questo repository e aiutami a usare IdeaFlow.
Ho un'idea su [descrivi brevemente].
Iniziamo dalla fase 1 (CAPTURE).
```

Oppure dai a Claude il link al repository:
> "Leggi https://github.com/disoardi/ideaflow/blob/main/AI.md e aiutami a usare il framework per gestire le mie idee"

---

## La struttura delle idee

Ogni idea passa attraverso questi stati:

```
Catturata → In Elaborazione → Pronta per Validazione
                                        ↓
                               GO ───► Da Fare → Documentata → Pronta per Implementazione
                               NO-GO → Rifiutata
```

Un file di tracker (`idea-tracker.md`) tiene traccia di tutte le tue idee e il loro stato.

---

## File importanti

```
templates/
├── prompts/          → I 5 prompt da usare con l'AI
│   ├── 01-capture.md
│   ├── 02-elaborate.md
│   ├── 03-validate.md
│   ├── 04-document.md
│   └── 05-prepare.md
└── core/
    ├── idea-tracker.md   → Tieni traccia di tutte le idee
    └── idea-template.md  → Template per una singola idea

AI.md           → Guida per AI e bot che leggono questo repo
docs/           → Documentazione completa
```

---

## Documentazione completa

- [Come iniziare](getting-started.md) — Tutorial passo-passo
- [Guida al workflow](workflow-guide.md) — Dettagli su ogni fase
- [Best practices](best-practices.md) — Consigli per usare al meglio il framework
- [Personalizzazione](customization.md) — Adatta il framework alle tue esigenze
- [FAQ](faq.md) — Domande frequenti

---

## Per AI e Bot

Se sei un'AI che ha ricevuto il link a questo repository, leggi [AI.md](../AI.md) — contiene istruzioni specifiche per capire e usare il framework con l'utente.

---

*IdeaFlow è open-source — [contribuisci su GitHub](https://github.com/disoardi/ideaflow)*
