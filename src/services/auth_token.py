import sqlite3 as sqlite
import model_create as model_create
from core.log import log

CREATE_STRING = """CREATE TABLE IF NOT EXISTS tokens (
    id INTEGER PRIMARY KEY,
    token TEXT NOT NULL
)"""

def __createNewToken(token):
    """creates a new one."""
    try:
        with sqlite.connect("data.db") as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO tokens (token) VALUES (?)", (token,))
            conn.commit()
            log("New token created successfully.")
    except sqlite.Error as e:
        log(f"Database error: {e}", 3)
        return None

def run():
    """Responsible for the tokens of the models"""
    log("Data Manager running.")
    try:
        with sqlite.connect("data.db") as conn:
            cursor = conn.cursor()
            cursor.execute(CREATE_STRING)
            conn.commit()
            log("Database initialized successfully.")
    except sqlite.Error as e:
        log(f"Database error: {e}", 3)
        return False
    return True

def getToken(config):
    """Retrieves the current token from the database, or creates a new one if none exists."""
    try:
        with sqlite.connect("data.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT token FROM tokens LIMIT 1")
            result = cursor.fetchone()
            if result:
                return result[0]
            else:
                token = model_create.createModel(config)
                log("Creating token")
                if token:
                    __createNewToken(token)
                    return token
                else:
                    log("Failed to create token.", 3)
                    return None
    except sqlite.Error as e:
        log(f"Database error: {e}", 3)
        return None
    
