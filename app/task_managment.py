import sqlite3
from datetime import datetime
from fastapi import HTTPException

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

def create_task(title: str,
    description: Optional[str],
    starts: Optional[datetime],
    due_date: Optional[datetime],
    is_done: bool,
    level: Literal["easy", "medium", "hard"],
    priority: Literal["low","normal","high"]):
    connection = get_connection()
    cur = connection.cursor()
    starts_text = starts.isoformat() if starts else None
    due_date_text = due_date.isoformat() if due_date else None
    is_done_int = 1 if is_done else 0

    cur.execute(
        "INSERT INTO tasks (title, description,starts,due_date,is_done,level,priority) VALUES (?,?,?,?,?,?,?)",
        (title,description,starts,due_date,done,level,priority),
    )

    connection.commit()
    task_id = cur.lastrowid
    cur.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
    row = cur.fetchone()
    connection.close()

    return row_to_dict(row)

def get_list_of_tasks():
    connection = get_connection()
    cur = connection.cursor()

    cur.execute("SELECT * FROM tasks ORDER BY id")

    rows = cur.fetchall()
    connection.close()
    return [row_to_dict(r) for r in rows]


def get_task_by_id(id):
    connection = get_connection()
    cur = connection.cursor()

    cur.execute("SELECT * FROM tasks WHERE id=?",(id,))

    rows = cur.fetchall()
    connection.close()
    if not row:
        raise HTTPException(status_code=404, detail="not found")
    return [row_to_dict(r) for r in rows]