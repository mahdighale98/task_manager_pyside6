import sqlite3
from datetime import date

class Task:
    """Represents a task item."""

    def __init__(
        self, 
        title: str, 
        due_date: str, 
        description: str = None, 
        status: str = "Not done"
    ):

        self.title = title
        self.status = status
        self.description = description

        # Validate date format (YYYY-MM-DD)
        try:
            due = date.fromisoformat(due_date)

        except ValueError:
            raise ValueError ("Invalid date format (yyyy-mm-dd)")
            
        self.due_date = due.isoformat()



class Database:
    """Handles database operations."""

    def __init__(self):
        
        self.connect = sqlite3.connect("task_base.db")
        self.cursor = self.connect.cursor()

        self._create_table()

    def _create_table(self):
        """Create tasks table if it does not exist."""

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        description TEXT,
                        due_date TEXT,
                        status TEXT              
                )
            """)
        self.connect.commit()

    def add_task(self, task: Task):
        """Insert a new task."""
        
        self.cursor.execute("""
            INSERT INTO tasks (title, description, due_date, status)
                    VALUES (?, ?, ?, ?)""", 
            (task.title, task.description, task.due_date, task.status)
            )
        
        self.connect.commit()

    def show_tasks(self):
        """Return all tasks."""

        self.cursor.execute("""
            SELECT * FROM tasks 
            """)
        
        return self.cursor.fetchall()
    
    def edit_task(
            self, 
            task_id: int, 
            title: str, 
            description: str, 
            due_date: str
    ):
        """Update task information."""

        self.cursor.execute("""
            UPDATE tasks 
            SET title = ?, description = ?, due_date = ? 
            WHERE id = ?""",
            (title, description, due_date, task_id))
        
        self.connect.commit()

    def close(self):
        """Close database connection."""
        
        self.connect.close()