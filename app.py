from flask import Flask, render_template, request, redirect, url_for
from db import get_db_connection, init_db

app = Flask(__name__)


# ------------------------------------
# Route 1: GET / — Show all expenses
# ------------------------------------
@app.route("/")
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, title, amount, category, date FROM expenses ORDER BY date DESC")
    expenses = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("index.html", expenses=expenses)


# ------------------------------------
# Route 2: POST /add — Add new expense
# ------------------------------------
@app.route("/add", methods=["POST"])
def add_expense():
    title = request.form["title"]
    amount = request.form["amount"]
    category = request.form["category"]
    date = request.form["date"]

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO expenses (title, amount, category, date) VALUES (%s, %s, %s, %s)",
        (title, amount, category, date)
    )
    conn.commit()
    cur.close()
    conn.close()

    return redirect(url_for("index"))


# ----------------------------------------
# Route 3: POST /delete/<id> — Delete one
# ----------------------------------------
@app.route("/delete/<int:id>", methods=["POST"])
def delete_expense(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM expenses WHERE id = %s", (id,))
    conn.commit()
    cur.close()
    conn.close()

    return redirect(url_for("index"))


# ------------------------------------
# Entry point
# ------------------------------------
if __name__ == "__main__":
    init_db()  # Ensure table exists on startup
    app.run(debug=True)
