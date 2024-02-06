from sqlalchemy import create_engine, text

# Create engine
engine = create_engine('mysql+pymysql://admin:test123@localhost/alieat',echo=True)

with engine.connect() as connection:
    result = connection.execute(text("SELECT 1"))
    print(result.fetchone())