# Human–AI Memory Continuity System (PS3 MVP)

A web-based **Human–AI Memory Continuity System** that preserves **decision context, reasoning, and uncertainty** so humans can later recall *why* a decision was made — not just *what* was decided.

This project is a **PS3-aligned proof of concept**, focused on explainability, ethical restraint, and human-in-the-loop decision support.

---

## Core Idea

Most tools store decisions as static outcomes.  
This system stores decisions as **reasoned events**, including:
- the goal
- constraints
- reasoning
- confidence (explicit uncertainty)

When a similar situation arises, the system recalls relevant past decisions and **explains why they may be relevant**, without making decisions for the user.

---

## Key Features

- **Decision Capture**  
  Record goal, constraints, options, reasoning, and confidence.

- **Persistent Decision Memory**  
  Decisions are stored with timestamps and remain fully inspectable.

- **Signal Extraction (Explainable)**  
  Explicit keywords (“decision signals”) are extracted from human reasoning.

- **Context-Aware Assist**  
  New situations are matched against past decision signals to recall relevant decisions with explanation.

---

## What This System Does NOT Do

- No autonomous decision-making  
- No behavioral profiling  
- No machine learning or black-box models  
- No prediction of user intent  

The human remains fully in control.

---

## Architecture (High Level)

User Input (Web)
↓
Decision Context + Reasoning
↓
Signal Extraction
↓
Persistent Memory (JSON)
↓
Context-Aware Recall (Explainable)


---

## Tech Stack

- Python 3  
- Flask  
- HTML + CSS  
- JSON storage  

No external AI services or ML models are used.

---

## How to Run

```bash
pip install flask
python app.py
http://127.0.0.1:5000

'''bash
- - -

##Ethics & Scope

-Explicit human input only
-Transparent reasoning and uncertainty
-Designed for clarity over automation
-This is a single-user prototype intended for ethical exploration of Human–AI memory continuity.

##Author

Solo hackathon project
Built for PS3: Human–AI Memory Continuity
