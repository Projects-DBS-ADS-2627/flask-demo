# database/

- `ddl.sql`: the CREATE TABLE statements of your group's database. Keep it up to date
  with every change, so that anyone can rebuild the tables from it.
- `dump.sql`: a backup of the database at the deadline, made with mysqldump:

```
mysqldump -h <host> -u <user> -p <database> > database/dump.sql
```

It asks for the password. Do not put the password on the command line or in this file.
