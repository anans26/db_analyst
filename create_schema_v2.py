from db import engine

files = [
    "schema/layer4.sql"
]

with engine.raw_connection() as conn:

    cursor = conn.cursor()

    for file_name in files:

        with open(file_name, "r") as file:
            sql = file.read()

        cursor.execute(sql)

    conn.commit()

print("Schema created successfully!")