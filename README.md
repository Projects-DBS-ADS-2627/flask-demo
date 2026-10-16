# Name of your application

One or two sentences: what it does, and for whom.

**Group:** PR2627-?  
**Client:** name and organisation, or "none, we test with" and who you test with

## Team

Everyone adds their own line, in their own commit.

| Name | GitHub account | Works on |
|---|---|---|
| | | |

## Install and run

You need Python, set up as on 23 September, and your group's database details from Ufora.

```
git clone <the URL of this repository>
cd <this folder>
```

| What | macOS, Linux | Windows |
|---|---|---|
| Make the environment | `python3 -m venv venv` | `py -m venv venv` |
| Activate it | `source venv/bin/activate` | `venv\Scripts\activate` |
| Install | `pip install -r requirements.txt` | `pip install -r requirements.txt` |

Then copy `.env.example` to `.env`, fill in the database details, and check the connection:

```
python check_db.py
flask --app app run --debug
```

Open http://127.0.0.1:5000.

## Links

- User interface prototype: 
- Board: 
- Anything else we want you to see: 

## Contribution table

Per part of the application, who wrote it. The commit history has to agree with this table.

| Part | Written by |
|---|---|
| routes/... | |
| templates/... | |
| models.py | |
| database/ddl.sql | |
| Algorithm: ... | |

## What the repository contains by 18 December

- [ ] The Flask application
- [ ] The DDL for your tables, in `database/ddl.sql`
- [ ] Screenshots or images of the user interface prototype, in `docs/prototype/`
- [ ] The final version of the user stories, in `docs/user-stories.md`
- [ ] A database dump (mysqldump), in `database/dump.sql`
- [ ] This README: how to install and run, the links, the contribution table
- [ ] The peer review, submitted by each of you on Ufora

## Project structure

```
app.py              creates the application and registers the routes
config.py           reads .env
models.py           one class per table
routes/             one file per part of the application
templates/          base.html and one template per page
static/css/         your own styles, on top of Bootstrap
algorithm/          the core logic of your algorithm, without Flask
database/           ddl.sql and, at the end, dump.sql
docs/               user stories and prototype screenshots
check_db.py         tests the database connection on its own
.env.example        what your .env looks like, without the passwords
```
