from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from db import engine


files = [
    BASE_DIR / "schema" / "layer1.sql",
    BASE_DIR / "schema" / "layer2.sql",
    BASE_DIR / "schema" / "layer3.sql",
    BASE_DIR / "schema" / "layer4.sql"
]

with engine.raw_connection() as conn:
    cursor = conn.cursor()

    try:
        for file_name in files:

            with open(file_name, "r") as file:
                sql = file.read()

            cursor.execute(sql)

        conn.commit()
        print("Schema created successfully!")

    except Exception as e:
        conn.rollback()
        print(f"Error creating schema: {e}")

    finally:
        cursor.close()
