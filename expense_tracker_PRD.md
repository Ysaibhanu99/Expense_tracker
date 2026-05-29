# PRD — Expense Tracker (Day 1 Foundation Project)

---

## 1. Purpose

Build a functional Expense Tracker using Flask + MySQL.  
**Core goal:** Complete your first end-to-end CRUD project where you understand every single line.  
This is a foundation project — not a portfolio piece. Simplicity is the feature.

---

## 2. Success Criteria

By end of Day 1, you should be able to say:

> "I connected Flask to MySQL, inserted a row from a form, fetched all rows,
> displayed them in a table, and deleted a row — and I understand every line."

---

## 3. Tech Stack

| Layer      | Technology              |
|------------|-------------------------|
| Backend    | Python + Flask          |
| Database   | MySQL                   |
| DB Driver  | `mysql-connector-python`|
| Frontend   | Plain HTML + minimal CSS (no framework) |
| No extras  | No Bootstrap, no JS frameworks, no ORM |

---

## 4. Database Schema

**Database name:** `expense_db`

```sql
CREATE DATABASE expense_db;

USE expense_db;

CREATE TABLE expenses (
    id       INT AUTO_INCREMENT PRIMARY KEY,
    title    VARCHAR(100)   NOT NULL,
    amount   DECIMAL(10, 2) NOT NULL,
    category VARCHAR(50)    NOT NULL,
    date     DATE           NOT NULL
);
```

**Categories (hardcoded in HTML dropdown):**
Food, Transport, Study, Entertainment, Other

---

## 5. Routes

| Method | Route              | What it does                        |
|--------|--------------------|-------------------------------------|
| GET    | `/`                | Fetch all expenses from DB, render  |
| POST   | `/add`             | Insert new expense row into DB      |
| POST   | `/delete/<int:id>` | Delete expense row by ID            |

No edit route. No API. No JSON. Just these 3.

---

## 6. Pages / UI

### Single page: `index.html`

**Section 1 — Add Expense Form (top of page)**
- Fields: Title (text), Amount (number), Category (dropdown), Date (date input)
- One submit button: "Add Expense"
- Form action: `POST /add`

**Section 2 — Expenses Table (below form)**
- Columns: #, Title, Amount (₹), Category, Date, Action
- Action column: a "Delete" button per row
- Delete uses a small form with `POST /delete/<id>`
- If no expenses: show "No expenses yet."

**No charts. No summary. No filters. No search.**  
Those are future project features — not today.

---

## 7. Folder Structure

```
expense-tracker/
│
├── app.py               ← All Flask routes live here
├── db.py                ← MySQL connection logic (get_db_connection())
│
├── templates/
│   └── index.html       ← Single HTML page
│
└── static/
    └── style.css        ← Optional, minimal CSS only
```

---

## 8. Build Order (follow this exactly)

```
Step 1 → Create the MySQL DB and table. Verify in MySQL CLI.
Step 2 → Write db.py — just the connection function. Test it runs.
Step 3 → Write GET / route — fetch all rows, print to terminal first.
Step 4 → Write index.html — just the table, hardcode 1 test row to check layout.
Step 5 → Connect GET / to index.html — pass real DB data to template.
Step 6 → Add the form to index.html.
Step 7 → Write POST /add route — insert into DB, redirect to /.
Step 8 → Write POST /delete/<id> route — delete row, redirect to /.
Step 9 → Test all 3 operations end-to-end.
```

**Rule:** Do not move to the next step until the current step works.

---

## 9. Strictly Out of Scope

These are explicitly NOT part of Day 1. Do not add them.

- ❌ User login / authentication
- ❌ Edit / update expense
- ❌ Charts or graphs
- ❌ Monthly totals or summaries
- ❌ Search or filter
- ❌ Pagination
- ❌ Bootstrap or any CSS framework
- ❌ JavaScript (even a single line)
- ❌ Deployment

If you finish early and feel the urge to add one of these — write it down for the next project instead.

---

## 10. What This Teaches You

| Concept                        | Where you use it in Smart Attendance |
|-------------------------------|--------------------------------------|
| Flask route with GET           | Every page load in attendance system |
| Flask route with POST          | Submitting attendance, marks entry   |
| MySQL INSERT                   | Adding student, saving marks         |
| MySQL SELECT                   | Listing students, showing reports    |
| MySQL DELETE                   | Removing a student record            |
| Jinja2 template with for loop  | Rendering student lists, mark sheets |
| HTML form → Flask route        | Every form in the entire system      |
| Redirect after POST            | Standard pattern to prevent resubmit |

---

*PRD version: 1.0 | Project: Foundation Block 1 — CRUD + DB*
