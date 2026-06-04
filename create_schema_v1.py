from sqlalchemy import text
from db import engine

with open("schema/layer1.sql", "r") as file:
    sql = file.read()

with engine.connect() as conn:
    conn.execute(text(sql))
    conn.commit()

print("Layer 1 tables created successfully!")