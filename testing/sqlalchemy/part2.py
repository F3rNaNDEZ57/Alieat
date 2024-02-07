from sqlalchemy import create_engine, text , MetaData


engine = create_engine('mysql+pymysql://admin:test123@localhost/alieat')


# fetching rows
with engine.connect() as conn:
    result1 = conn.execute(text("SELECT * FROM test"))
    result2 = conn.execute(text("SELECT * FROM test2"))
    print("test1")
    for row in result1:
        print(f"id: {row.id}, name: {row.name}")

    print("\n")
    print("test2")
    for row in result2:
        print(f"id: {row.id}, name: {row.name}")    


# there is a few ways to assign row values to variables
        
# 1. tuple unpacking/assignment
print("\nTuple unpacking/assignment")
with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM test"))
    for x,y in result:
        print(f"id: {x}, name: {y}")


# 2. integer indexing
print("\nInteger indexing")
with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM test"))
    for row in result:
        print(f"id: {row[0]}, name: {row[1]}")

# 3. attribute name
print("\nAttribute name")
with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM test"))
    for row in result:
        print(f"id: {row.id}, name: {row.name}")

# 4. mapping access
print("\nMapping access")
with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM test"))
    for row in result.mappings():
        x = row['id']
        y = row['name']
        print(f"id: {x}, name: {y}")                