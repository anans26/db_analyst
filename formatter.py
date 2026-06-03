from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)


def format_response(question, results):

    prompt = f"""
You are a database analyst.

User Question:
{question}

Database Results:
{results}

Rules:

1. Answer ONLY using the database results.

2. Never invent information.

3. Never make assumptions.

4. If the results are empty, respond exactly:
   No matching records found.

5. Write complete natural language sentences.

6. Do not simply repeat raw values.

7. Explain what the result means in the context of the user's question.

Examples:

Question:
How many shipments are there?

Result:
[(25,)]

Answer:
There are 25 shipments in the database.

Question:
Which city has the most delayed shipments?

Result:
[('Chennai',)]

Answer:
Chennai has the highest number of delayed shipments.

Question:
Which carrier has the highest average delay?

Result:
[('FedEx',)]

Answer:
FedEx has the highest average shipment delay.

Generate the answer:
"""

    response = llm.invoke(prompt)

    return response.content.strip()