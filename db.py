import sqlite3

def connect_to_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

def initial_setup():
    conn = connect_to_db()
    conn.execute(
        """
        DROP TABLE IF EXISTS jobs;
        """
    )
    conn.execute(
        """
        CREATE TABLE jobs (
        id INTEGER PRIMARY KEY NOT NULL,
        title TEXT,
        company TEXT,
        location TEXT,
        description TEXT,
        salary TEXT
        );
        """
    )
    conn.commit()
    print("Table created successfully")

    jobs_seed_data = [
        ("Accountant","Verizon","New York, NY","Accountant for Verizon","50-100k"),
        ("Software Engineer","Google","Mountain View, CA","Develop and maintain scalable software systems","120-180k"),
        ("Data Analyst","Spotify","Boston, MA","Analyze music streaming trends and user behavior","80-120k"),
        ("Marketing Manager","Airbnb","San Francisco, CA","Lead brand marketing campaigns globally","100-150k"),
        ("UX Designer","Meta","Seattle, WA","Design intuitive user experiences for mobile apps","95-140k"),
        ("Financial Analyst","Goldman Sachs","New York, NY","Perform financial modeling and forecasting","90-130k"),
        ("Project Manager","Amazon","Austin, TX","Oversee logistics and supply chain initiatives","95-145k"),
        ("Product Manager","Netflix","Los Angeles, CA","Define product roadmap and drive execution","110-170k"),
        ("HR Specialist","Adobe","Denver, CO","Manage recruitment and employee relations","70-110k"),
        ("Cybersecurity Analyst","Cisco","Raleigh, NC","Protect systems and data from cyber threats","100-140k")
    ]
    conn.executemany(
        """
        INSERT INTO jobs (title, company, location, description, salary)
        VALUES (?,?,?,?,?)
        """,
        jobs_seed_data,
    )
    conn.commit()
    print("Seed data created successfully")

    conn.close()

if __name__ == "__main__":
    initial_setup()

def jobs_all():
    conn = connect_to_db()
    rows = conn.execute(
        """
        SELECT * FROM jobs
        """
    ).fetchall()
    return [dict(row) for row in rows]

def jobs_create(title, company, location, description, salary):
    conn = connect_to_db()
    row = conn.execute(
        """
        INSERT INTO jobs (title, company, location, description, salary)
        VALUES (?, ?, ?, ?, ?)
        RETURNING *
        """,
        (title, company, location, description, salary),
    ).fetchone()
    conn.commit()
    return dict(row)

def jobs_find_by_id(id):
    conn = connect_to_db()
    row = conn.execute(
        """
        SELECT * FROM jobs
        WHERE id = ?
        """,
        (id,),
    ).fetchone()
    return dict(row)