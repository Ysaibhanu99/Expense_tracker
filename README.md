# Expense Tracker

A simple expense tracker I built while learning Flask and databases. Nothing fancy — just a basic CRUD app where you can add expenses, see them in a table, and delete the ones you don't need.

I built this as my first proper project to understand how a backend actually connects to a database and renders stuff on the frontend. Before this I was just following tutorials without building anything real, so this was my way of actually applying what I learned.

The problem it solves is pretty straightforward — keeping track of where your money goes. I know there are a million apps for this already, but the point was to build one myself from scratch.

## Features

- Add an expense with title, amount, category, and date
- View all your expenses in a table (newest first)
- Delete any expense you dont need anymore
- Date auto-fills to today so you dont have to pick it every time
- Asks for confirmation before deleting (so you dont accidentally remove stuff)
- Categories are color coded so its easy to scan through
- Works on mobile too, mostly

## Tech Stack

| What | Technology |
|------|-----------|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python (Flask) |
| Database | PostgreSQL on Neon (serverless) |
| DB Driver | psycopg2 |

No frameworks on the frontend. No Bootstrap. Just plain HTML/CSS/JS. I wanted to understand how things work before adding layers on top.

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

## What I Learned

This was my first time connecting a backend to an actual cloud database, and honestly it was confusing at first. I kept getting SSL errors with Neon until I figured out the connection string format.

Some things I picked up along the way:
- How Flask routes work — GET for loading pages, POST for submitting forms
- Writing raw SQL queries instead of using an ORM (wanted to understand whats actually happening)
- The POST-Redirect-GET pattern — I didnt know this was a thing until I saw my form resubmitting data on every refresh
- Jinja2 templating — passing data from Python to HTML felt weird at first but it makes sense now
- How to structure a project with separate files for db logic and app logic instead of dumping everything in one file
- CSS variables and how to make a dark theme without it looking terrible

Its not perfect code but I actually understand every line of it, which was the whole point.

## Future Improvements

Some things I want to add when I come back to this project:

- Edit/update an expense (right now you can only add or delete)
- Monthly summary showing total spent
- Filter by category or date range
- Charts or graphs to visualize spending
- Maybe user login so multiple people can use it
- Better error handling (right now if the DB is down it just crashes lol)

## Note

This project was built purely for learning. Its part of my foundation projects where Im trying to get better at full stack development step by step. Its not meant to be production ready or anything like that — just me figuring things out and building stuff along the way.

If you're also learning and found this helpful, thats cool. Feel free to fork it or use it as a starting point for your own version.
