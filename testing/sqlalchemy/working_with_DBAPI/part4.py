from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session


engine = create_engine('mysql+pymysql://admin:test123@localhost/alieat')

# Executing with an ORM Session
stmt = text("SELECT id, name FROM test WHERE id > :id ORDER BY id, name")
stmt_insert = text("INSERT INTO test (id, name) VALUES (:id, :name)")
stmt_update = text("UPDATE test SET name = :name WHERE id = :id")

with Session(engine) as session:
    result = session.execute(stmt, {"id": 1})
    session.commit()

    for row in result:
        print(f"id: {row.id}, name: {row.name}")

    result = session.execute(stmt_insert,[{"id": 100, "name": "test10"},
                                          {"id": 101, "name": "test11"},
                                          {"id": 102, "name": "test12"},
                                          {"id": 103, "name": "test13"}]) 
    session.commit()

    print("\n")
    result = session.execute(stmt, {"id": 10})
    for row in result:
        print(f"id: {row.id}, name: {row.name}")   


    result = session.execute(stmt_update, {"id": 100, "name": "test100"})
    session.commit()

    print("\n")
    result = session.execute(stmt, {"id": 10})
    for row in result:
        print(f"id: {row.id}, name: {row.name}")    



