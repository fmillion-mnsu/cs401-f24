# Database init script for CS401 assignment 3

import os
import os.path
import sqlite3

def main():

    # Ensure user has not already initted database.
    # In a production app we could just exit here, but for the nature of the assignment,
    # this will ensure you set things up correctly.
    if os.path.isfile("/data/log.sqlite3"):
        print("The database is already initialized.")
        print("You did not take proper steps to ensure re-initialization doesn't occur.")
        print("Check your scripts and try again.")
        os.unlink("/data/log.sqlite3")
        open("/data/.invalid","a").close()
        exit(1)

    # If it was incorrect once, don't allow it again...
    if os.path.isfile("/data/.invalid"):
        print("You previously failed to check for the database already being initialized.")
        print("Check your scripts and try again.")
        exit(1)

    # Ok, go ahead and init the database
    ctx = sqlite3.connect("/data/log.sqlite3")
    cur = ctx.cursor()

    # Create the table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date REAL NOT NULL,
            endpoint TEXT NOT NULL
        )
    ''')

    ctx.commit()
    cur.close()
    ctx.close()

    print("The database has been initialized!")

if __name__ == "__main__":
    main()
