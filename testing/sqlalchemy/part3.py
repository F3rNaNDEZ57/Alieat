from sqlalchemy import create_engine, text , MetaData


engine = create_engine('mysql+pymysql://admin:test123@localhost/alieat')


# Sending parameters - single parameter
with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM test WHERE id >= :id"), {"id": 2})
    conn.commit()
    for row in result:
        print(f"id: {row.id}, name: {row.name}")    


# Sending parameters - multiple parameters
with engine.connect() as conn:
    #insert data
    result1 = conn.execute(text("INSERT INTO test (id, name) VALUES (:id, :name)"),
                           [{"id": 11, "name": "test11"}, {"id": 12, "name": "test12"}, {"id": 13, "name": "test13"}, {"id": 14, "name": "test14"}])
    conn.commit()
    
    
    #fetch data as a query
    result2 = conn.execute(text("SELECT * FROM test WHERE id >= :id AND name = :name"), {"id": 2, "name": "test2"})
    result3 = conn.execute(text("SELECT * FROM test WHERE id >= :id AND name = :name"), {"id": 12, "name": "test12"})
    conn.commit()

    print("\n\n")
    for row in result2:
        print(f"id: {row.id}, name: {row.name}")        
