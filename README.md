# Expense Tracker

A simple expense tracker I built while learning Flask and databases. Started as a basic CRUD app and then I kept adding stuff to it — now it has charts, filters, monthly summaries, edit functionality, the whole thing.

I built this as my first proper project to understand how a backend actually connects to a database and renders stuff on the frontend. Before this I was just following tutorials without building anything real, so this was my way of actually applying what I learned.

The problem it solves is pretty straightforward — keeping track of where your money goes. I know there are a million apps for this already, but the point was to build one myself from scratch.

## Features

- Add an expense with title, amount, category, and date
- Edit or update any existing expense
- Delete expenses (with confirmation so you dont accidentally nuke stuff)
- View all expenses in a table sorted by date
- Filter by category, date range, or both
- Monthly summary cards showing how much you spent each month
- Charts — doughnut chart for category breakdown, bar chart for monthly trends
- Grand total display across all expenses
- Flash messages for success/error feedback
- Date auto-fills to today
- Categories are color coded
- Error handling — app wont crash if the database is down, shows proper messages
- Dark theme with a pretty clean UI
- Works on mobile too, mostly

## Tech Stack

| What | Technology |
|------|-----------|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python (Flask) |
| Database | PostgreSQL on Neon (serverless) |
| DB Driver | psycopg2 |
| Charts | Chart.js |
| Deployment | Render |

No frameworks on the frontend. No Bootstrap. Just plain HTML/CSS/JS and Chart.js for the graphs. I wanted to understand how things work before adding layers on top.

## Screenshots

> I'll add screenshots here once I get around to it. For now just clone it and run it locally lol.

## How to Run

You'll need Python installed on your machine. Also you need a Neon account (its free) to get a database URL.

1. **Clone the repo**
   ```
   git clone https://github.com/Ysaibhanu99/Expense_tracker.git
   cd Expense_tracker
   ```

2. **Install the dependencies**
   ```
   pip install -r requirements.txt
   ```

3. **Set up your database**

   Go to [neon.tech](https://neon.tech), create a free project, and copy your connection string.

4. **Create a `.env` file** in the root folder and paste your connection string:
   ```
   DATABASE_URL=postgresql://your_user:your_password@your_host/your_db?sslmode=require
   ```

5. **Run the app**
   ```
   python app.py
   ```

6. Open `http://127.0.0.1:5000` in your browser and you should see it running.

The table gets created automatically when you start the app for the first time so you dont need to run any SQL manually.

## Live Demo

This app is deployed on Render. The database runs on Neon (serverless PostgreSQL).

If you want to deploy your own version:
1. Fork this repo
2. Create a free account on [render.com](https://render.com)
3. Create a new Web Service and connect your GitHub repo
4. Set the build command to `pip install -r requirements.txt`
5. Set the start command to `gunicorn app:app`
6. Add `DATABASE_URL` as an environment variable with your Neon connection string
7. Hit deploy and wait a couple minutes

## What I Learned

This was my first time connecting a backend to an actual cloud database, and honestly it was confusing at first. I kept getting SSL errors with Neon until I figured out the connection string format.

Some things I picked up along the way:
- How Flask routes work — GET for loading pages, POST for submitting forms
- Writing raw SQL queries instead of using an ORM (wanted to understand whats actually happening)
- The POST-Redirect-GET pattern — I didnt know this was a thing until I saw my form resubmitting data on every refresh
- Jinja2 templating — passing data from Python to HTML felt weird at first but it makes sense now
- How to structure a project with separate files for db logic and app logic instead of dumping everything in one file
- CSS variables and how to make a dark theme without it looking terrible
- Chart.js — rendering graphs from database data passed through Flask
- Filtering with SQL query params — building dynamic WHERE clauses
- Flash messages in Flask for user feedback
- Deploying a Flask app on Render with gunicorn

Its not perfect code but I actually understand every line of it, which was the whole point.

## Future Improvements

Most of the stuff I originally planned is already done now (edit, charts, filters, summary, error handling). Some things I might add later if I feel like it:

- User login so multiple people can track their own expenses
- Export to CSV or PDF
- Recurring expenses (like subscriptions that repeat every month)
- Budget limits per category with alerts
- A dashboard with more detailed analytics

## Note

This project was built purely for learning. Its part of my foundation projects where Im trying to get better at full stack development step by step. Its not meant to be production ready or anything like that — just me figuring things out and building stuff along the way.

If you're also learning and found this helpful, thats cool. Feel free to fork it or use it as a starting point for your own version.
