import sqlite3
from datetime import datetime

DB_NAME = "faith.db"

class Registration:
    def __init__(self, id=None, name=None, email=None, phone=None, church=None, created_at=None):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.church = church
        self.created_at = created_at or datetime.now()
