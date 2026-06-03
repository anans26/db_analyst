FORBIDDEN = [
    "INSERT",
    "UPDATE",
    "DELETE",
    "DROP",
    "ALTER",
    "CREATE",
    "TRUNCATE",
    "GRANT",
    "REVOKE"
]

ALLOWED_TABLES = [
    "SHIPMENTS"
]


def validate_sql(query):

    query_upper = query.upper().strip()

    # Must be a SELECT query
    if not query_upper.startswith("SELECT"):
        return False

    # Must contain FROM clause
    if "FROM " not in query_upper:
        return False

    # Block joins (single-table project)
    if "JOIN" in query_upper:
        return False

    # Block UNION queries
    if "UNION" in query_upper:
        return False

    # Extract table name
    table_name = (
        query_upper
        .split("FROM ")[1]
        .split()[0]
        .replace(";", "")
    )

    # Only allow shipments table
    if table_name not in ALLOWED_TABLES:
        return False

    # Block dangerous keywords
    for keyword in FORBIDDEN:
        if keyword in query_upper:
            return False

    return True

