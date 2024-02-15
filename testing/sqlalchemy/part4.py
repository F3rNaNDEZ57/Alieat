from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session


engine = create_engine('mysql+pymysql://admin:test123@localhost/alieat')

# Executing with an ORM Session
stmt = text("SELECT id, name FROM test WHERE id > :id ORDER BY id, name")

with Session(engine) as session:
    result = session.execute(stmt, {"id": 1})
    for row in result:
        print(f"id: {row.id}, name: {row.name}")



