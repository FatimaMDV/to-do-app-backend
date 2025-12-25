from typing import Optional, List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import sqlite3


database_file = "todo.db"
def init_database():
    connection = sqlite3.connect(database_file)
    connection.execute("""
        CREATE TABLE IF NOT EXISTS TASKS(
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
