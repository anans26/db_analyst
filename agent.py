from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

SCHEMA = """
Table: shipments

Columns:
shipment_id
order_date
delivery_date
city
carrier
status
delay_days
shipping_cost
customer_segment
"""


def clean_sql(sql):
    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")
    return sql.strip()


def generate_sql(question):

    prompt = f"""
You are a PostgreSQL analyst.

Database Schema:

{SCHEMA}

Rules:

1. Generate ONLY SQL.

2. Return raw SQL only.

3. Do NOT use markdown code blocks.

4. Use ONLY the shipments table.

5. Use ONLY columns listed in the schema.

6. Generate SELECT queries only.

7. If the user requests any operation that modifies data such as:
   INSERT
   UPDATE
   DELETE
   DROP
   ALTER
   CREATE
   TRUNCATE
   GRANT
   REVOKE

   Respond ONLY with:

   MODIFICATION_NOT_ALLOWED

8. If the question cannot be answered using the schema,
   respond ONLY with:

   CANNOT_ANSWER

9. Never invent tables.

10. Never invent columns.

11. Never invent values.

12. Use only the provided schema.

13. If the query can be answered, generate a valid PostgreSQL SELECT query.

Question:
{question}
"""

    response = llm.invoke(prompt)

    sql = clean_sql(
        response.content
    )

    return sql

