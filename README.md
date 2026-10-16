# Class bookings, the Flask demo

The demo application from the Flask lectures of Algorithms and Data Structures
(weeks 5 and 6). Members of a gym book a spot in a class. It is the example on the
slides: `GymClass`, `Booking`, `routes/classes.py`.

It started from `project-template`, the same repository your group got. Compare
the two and you see exactly what was added, file by file.

## Follow it step by step

Every step is a commit with a tag. Check out a tag to see the application as it
was at that point in the lecture.

| Tag | What it adds | Slides |
|---|---|---|
| `start` | The template, untouched | |
| `step-1` | A route in `routes/classes.py` and a template, data still in a Python list | 05b, slides 5 to 8 |
| `step-2` | The data from the database: `models.py`, `database/ddl.sql`, a detail page | 05b, slides 6, 7, 10, 11 |
| `step-3` | Booking a spot: a form, a POST, check, write, redirect | 06b, slides 3 to 7 |
| `step-4` | Bootstrap, and the pages nobody designs: empty, full, not found | 06b, slides 8 to 11 |

```
git checkout step-2      # go to a step
git checkout main        # back to the end
git diff step-1 step-2   # what changed between two steps
```

Notice what does not change between `step-1` and `step-2`: the template. The route
gets its data somewhere else, and the view does not need to know.

## Install and run

You need Python, set up as on 23 September, and a database you can use for tests.

```
git clone https://github.com/Projects-DBS-ADS-2627/flask-demo.git
cd flask-demo
```

| What | macOS, Linux | Windows |
|---|---|---|
| Make the environment | `python3 -m venv venv` | `py -m venv venv` |
| Activate it | `source venv/bin/activate` | `venv\Scripts\activate` |
| Install | `pip install -r requirements.txt` | `pip install -r requirements.txt` |

Copy `.env.example` to `.env` and fill in the database details. Then:

```
python check_db.py                # prints ok
python database/load_demo_data.py # creates the three tables with test data
flask --app app run --debug
```

Open http://127.0.0.1:5000/classes.

`load_demo_data.py` drops and recreates the tables `member`, `gym_class` and
`booking`. Run it against a test database, not against the database of your
group project.

## Project structure

```
app.py              creates the application and registers the routes
config.py           reads .env
models.py           Member, GymClass, Booking: one class per table
routes/main.py      the start page
routes/classes.py   the list, the detail page and the booking
templates/          base.html, classes.html, class.html, 404.html
database/ddl.sql    the tables and the test data
check_db.py         tests the database connection on its own
```
