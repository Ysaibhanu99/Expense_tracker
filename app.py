from flask import Flask, render_template, request, redirect, url_for, flash
from db import get_db_connection, init_db
from datetime import datetime, date
from decimal import Decimal
import json

app = Flask(__name__)
app.secret_key = "expense-tracker-secret-key-2026"


# ------------------------------------
# Route 1: GET / — Show all expenses
# ------------------------------------
@app.route("/")
def index():
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        # --- Build filtered query ---
        query = "SELECT id, title, amount, category, date FROM expenses WHERE 1=1"
        params = []

        # Filter by category
        filter_category = request.args.get("category", "")
        if filter_category:
            query += " AND category = %s"
            params.append(filter_category)

        # Filter by date range
        filter_date_from = request.args.get("date_from", "")
        filter_date_to = request.args.get("date_to", "")
        if filter_date_from:
            query += " AND date >= %s"
            params.append(filter_date_from)
        if filter_date_to:
            query += " AND date <= %s"
            params.append(filter_date_to)

        query += " ORDER BY date DESC"
        cur.execute(query, params)
        expenses = cur.fetchall()

        # --- Monthly summary ---
        cur.execute("""
            SELECT
                TO_CHAR(date, 'YYYY-MM') AS month,
                SUM(amount) AS total
            FROM expenses
            GROUP BY TO_CHAR(date, 'YYYY-MM')
            ORDER BY month DESC
        """)
        monthly_summary = cur.fetchall()

        # --- Category totals (for charts) ---
        cur.execute("""
            SELECT category, SUM(amount) AS total
            FROM expenses
            GROUP BY category
            ORDER BY total DESC
        """)
        category_totals = cur.fetchall()

        # --- Monthly totals (for bar chart) ---
        cur.execute("""
            SELECT
                TO_CHAR(date, 'YYYY-MM') AS month,
                SUM(amount) AS total
            FROM expenses
            GROUP BY TO_CHAR(date, 'YYYY-MM')
            ORDER BY month ASC
        """)
        monthly_chart_data = cur.fetchall()

        # --- Grand total ---
        cur.execute("SELECT COALESCE(SUM(amount), 0) FROM expenses")
        grand_total = cur.fetchone()[0]

        cur.close()
        conn.close()

        # Prepare chart data as JSON for JavaScript
        chart_category_labels = json.dumps([row[0] for row in category_totals])
        chart_category_values = json.dumps([float(row[1]) for row in category_totals])
        chart_monthly_labels = json.dumps([row[0] for row in monthly_chart_data])
        chart_monthly_values = json.dumps([float(row[1]) for row in monthly_chart_data])

        return render_template(
            "index.html",
            expenses=expenses,
            monthly_summary=monthly_summary,
            grand_total=grand_total,
            filter_category=filter_category,
            filter_date_from=filter_date_from,
            filter_date_to=filter_date_to,
            chart_category_labels=chart_category_labels,
            chart_category_values=chart_category_values,
            chart_monthly_labels=chart_monthly_labels,
            chart_monthly_values=chart_monthly_values,
        )

    except Exception as e:
        flash(f"Error loading expenses: {e}", "error")
        return render_template(
            "index.html",
            expenses=[],
            monthly_summary=[],
            grand_total=0,
            filter_category="",
            filter_date_from="",
            filter_date_to="",
            chart_category_labels="[]",
            chart_category_values="[]",
            chart_monthly_labels="[]",
            chart_monthly_values="[]",
        )


# ------------------------------------
# Route 2: POST /add — Add new expense
# ------------------------------------
@app.route("/add", methods=["POST"])
def add_expense():
    try:
        title = request.form["title"].strip()
        amount = request.form["amount"]
        category = request.form["category"]
        expense_date = request.form["date"]

        if not title:
            flash("Title cannot be empty.", "error")
            return redirect(url_for("index"))

        if float(amount) <= 0:
            flash("Amount must be greater than 0.", "error")
            return redirect(url_for("index"))

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO expenses (title, amount, category, date) VALUES (%s, %s, %s, %s)",
            (title, amount, category, expense_date)
        )
        conn.commit()
        cur.close()
        conn.close()

        flash("Expense added successfully!", "success")

    except ValueError:
        flash("Invalid amount entered.", "error")
    except Exception as e:
        flash(f"Error adding expense: {e}", "error")

    return redirect(url_for("index"))


# ----------------------------------------
# Route 3: POST /delete/<id> — Delete one
# ----------------------------------------
@app.route("/delete/<int:id>", methods=["POST"])
def delete_expense(id):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM expenses WHERE id = %s", (id,))
        conn.commit()
        cur.close()
        conn.close()

        flash("Expense deleted.", "success")

    except Exception as e:
        flash(f"Error deleting expense: {e}", "error")

    return redirect(url_for("index"))


# ------------------------------------------
# Route 4: GET /edit/<id> — Show edit form
# ------------------------------------------
@app.route("/edit/<int:id>")
def edit_expense(id):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, title, amount, category, date FROM expenses WHERE id = %s", (id,))
        expense = cur.fetchone()
        cur.close()
        conn.close()

        if not expense:
            flash("Expense not found.", "error")
            return redirect(url_for("index"))

        return render_template("edit.html", expense=expense)

    except Exception as e:
        flash(f"Error loading expense: {e}", "error")
        return redirect(url_for("index"))


# ------------------------------------------
# Route 5: POST /edit/<id> — Update expense
# ------------------------------------------
@app.route("/edit/<int:id>", methods=["POST"])
def update_expense(id):
    try:
        title = request.form["title"].strip()
        amount = request.form["amount"]
        category = request.form["category"]
        expense_date = request.form["date"]

        if not title:
            flash("Title cannot be empty.", "error")
            return redirect(url_for("edit_expense", id=id))

        if float(amount) <= 0:
            flash("Amount must be greater than 0.", "error")
            return redirect(url_for("edit_expense", id=id))

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "UPDATE expenses SET title = %s, amount = %s, category = %s, date = %s WHERE id = %s",
            (title, amount, category, expense_date, id)
        )
        conn.commit()
        cur.close()
        conn.close()

        flash("Expense updated successfully!", "success")

    except ValueError:
        flash("Invalid amount entered.", "error")
        return redirect(url_for("edit_expense", id=id))
    except Exception as e:
        flash(f"Error updating expense: {e}", "error")

    return redirect(url_for("index"))


# ------------------------------------
# Entry point
# ------------------------------------
if __name__ == "__main__":
    init_db()  # Ensure table exists on startup
    app.run(debug=True)
