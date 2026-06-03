import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="logistics_ai",
    user="postgres",
    password="postgres",
    port=5433
)

cursor = conn.cursor()

# Remove old table if it exists
cursor.execute("""
DROP TABLE IF EXISTS shipments;
""")

# Create new table
cursor.execute("""
CREATE TABLE shipments (
    shipment_id SERIAL PRIMARY KEY,
    order_date DATE,
    delivery_date DATE,
    city VARCHAR(50),
    carrier VARCHAR(50),
    status VARCHAR(20),
    delay_days INT,
    shipping_cost DECIMAL(10,2),
    customer_segment VARCHAR(30)
);
""")

conn.commit()

print("Shipments table created successfully!")

cursor.close()
conn.close()