-- The DDL of the demo database. This file is the truth:
-- change a table here first, run it, then change the class in models.py.
--
-- Run it against your database from the client you use for Database Systems,
-- or with: python database/load_demo_data.py
-- It drops and recreates the three demo tables, so the demo always starts the same.

DROP TABLE IF EXISTS booking;
DROP TABLE IF EXISTS gym_class;
DROP TABLE IF EXISTS member;

CREATE TABLE member (
    id    INT AUTO_INCREMENT PRIMARY KEY,
    name  VARCHAR(80) NOT NULL
);

CREATE TABLE gym_class (
    id         INT AUTO_INCREMENT PRIMARY KEY,
    name       VARCHAR(80) NOT NULL,
    starts_at  DATETIME NOT NULL,
    capacity   INT NOT NULL
);

CREATE TABLE booking (
    id         INT AUTO_INCREMENT PRIMARY KEY,
    member_id  INT NOT NULL,
    class_id   INT NOT NULL,
    FOREIGN KEY (member_id) REFERENCES member(id),
    FOREIGN KEY (class_id) REFERENCES gym_class(id),
    UNIQUE (member_id, class_id)
);

-- Test data. It does not have to be sensible, it has to be there.

INSERT INTO member (name) VALUES
    ('Lotte'), ('Ward'), ('Amira'), ('Jonas'), ('Fien');

INSERT INTO gym_class (name, starts_at, capacity) VALUES
    ('Spinning', '2026-10-21 18:00:00', 12),
    ('Yoga',     '2026-10-22 07:30:00', 8),
    ('Boxing',   '2026-10-23 19:00:00', 10),
    ('Pilates',  '2026-10-24 10:00:00', 2);

INSERT INTO booking (member_id, class_id) VALUES
    (1, 1), (2, 1), (3, 1),
    (2, 2),
    (4, 4), (5, 4);
