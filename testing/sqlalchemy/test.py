from sqlalchemy import create_engine, text , MetaData

# Create engine
engine = create_engine('mysql+pymysql://admin:test123@localhost/alieat')

with engine.connect() as connection:
    result = connection.execute(text("SELECT 1"))
    print(result.fetchone())


# Reflecting the database and printing the table names and column names
metadata = MetaData()
metadata.reflect(bind=engine)


for table_name, table in metadata.tables.items():
    column_names = ', '.join([column.name for column in table.columns])
    print(f"{table_name}({column_names})")


# Inserting data into the database
