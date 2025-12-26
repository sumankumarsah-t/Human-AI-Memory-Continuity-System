from flask import Flask, render_template, request, redirect, url_for
import json
import os
from datetime import datetime

app = Flask(__name__)

DATA_FILE = os.path.join("storage", "decisions.json")

# ---------- Utility Functions ----------

def load_decisions():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_decisions(decisions):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(decisions, f, indent=2)

def extract_signals(text):
    stopwords = {
        "the", "and", "or", "to", "of", "a", "in", "for", "with", "on"
    }
    words = text.lower().split()
    return list({w for w in words if w not in stopwords and len(w) > 3})



# ---------- Routes ----------

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_decision():
    if request.method == "POST":
        decisions = load_decisions()

        decision = {
            "decision_id": f"D{len(decisions) + 1}",
            "timestamp": datetime.now().isoformat(),
            "goal": request.form.get("goal"),
            "constraints": request.form.get("constraints"),
            "options": [o.strip() for o in request.form.get("options").split(",")],
            "chosen_option": request.form.get("chosen_option"),
            "confidence": float(request.form.get("confidence")),
            "reasoning": request.form.get("reasoning"),
            "signals": extract_signals(
    (request.form.get("goal") or "") + " " +
    (request.form.get("constraints") or "") + " " +
    (request.form.get("reasoning") or "")
)

        }

        decisions.append(decision)
        save_decisions(decisions)

        return redirect(url_for("recall"))

    return render_template("add.html")


@app.route("/recall")
def recall():
    decisions = load_decisions()
    return render_template("recall.html", decisions=decisions)

@app.route("/assist", methods=["GET", "POST"])
def assist():
    explanation = None

    if request.method == "POST":
        user_context = request.form.get("context", "")
        context_signals = extract_signals(user_context)

        decisions = load_decisions()
        best_match = None
        best_score = 0
        matched_signals = []

        for d in decisions:
            decision_signals = set(d.get("signals", []))
            overlap = decision_signals & set(context_signals)

            if len(overlap) > best_score:
                best_score = len(overlap)
                best_match = d
                matched_signals = list(overlap)

        if best_match:
            explanation = (
                f"This situation matches a previous decision where you chose "
                f"'{best_match['chosen_option']}' for the goal "
                f"'{best_match['goal']}'.\n\n"
                f"Matched signals: {matched_signals}\n"
                f"Confidence at the time: {best_match['confidence']}\n"
                f"Reasoning: {best_match['reasoning']}"
            )

    return render_template("assist.html", explanation=explanation)

# ---------- Run Server ----------

if __name__ == "__main__":
    app.run(debug=True)
