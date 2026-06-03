from sqlalchemy import text

from agent import generate_sql
from validator import validate_sql
from db import engine
from formatter import format_response


question = input("Ask a question: ")

sql = generate_sql(question)

print("\nGenerated SQL:")
print(sql)

# Handle special responses
if sql == "MODIFICATION_NOT_ALLOWED":
    print(
        "This assistant supports read-only analytics and cannot modify database records."
    )
    exit()

if sql == "CANNOT_ANSWER":
    print(
        "The requested information is not available in the database."
    )
    exit()

# Validate generated SQL
if not validate_sql(sql):
    print(
        "Unsafe query detected."
    )
    exit()

try:

    with engine.connect() as conn:

        result = conn.execute(
            text(sql)
        )

        rows = result.fetchall()

        if not rows:

            print(
                "No matching records found."
            )

        else:

            answer = format_response(
                question,
                rows
            )

            print("\nBot:")
            print(answer)

except Exception as e:

    print(
        "\nDatabase error occurred."
    )

    print(f"Error: {e}")