import sqlite3

database_file = "todo.db"

def get_connection():
    connection = sqlite3.connect(database_file)
    connection.row_factory = sqlite3.Row
    return connection

def init_database():
    connection = get_connection()
    connection.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            is_done INTEGER NOT NULL DEFAULT 0,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            starts TEXT,
            due_date TEXT,
            level TEXT,
            priority TEXT
        );
    """)
    connection.commit()
    connection.close()

def row_to_dict(row):
    return {
        "id": row["id"],
        "title": row["title"],
        "description": row["description"],
        "is_done": bool(row["is_done"]),
        "created_at": row["created_at"],
        "updated_at": row["updated_at"],
        "starts": row["starts"],
        "due_date": row["due_date"],
        "level": row["level"],
        "priority": row["priority"],
    }

