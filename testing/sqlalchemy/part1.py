from sqlalchemy import create_engine, text , MetaData

# Create engine
engine = create_engine('mysql+pymysql://admin:test123@localhost/alieat')

# Getting a connection
with engine.connect() as connection:
    result = connection.execute(text("SELECT 1"))
    print(result.fetchone())
    result = connection.execute(text("SELECT 'Hello, World!'"))
    print(result.all())


# Commiting changes
# commit as you go
with engine.connect() as conn:
    conn.execute(text("CREATE TABLE test (id int, name varchar(50))"))
    conn.execute(text("INSERT INTO test (id, name) VALUES (:id, :name)"),
                  [{"id": 1, "name": "test1"}, {"id": 2, "name": "test2"}]
                  ) 
    conn.commit()  



