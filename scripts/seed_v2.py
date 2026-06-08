from pathlib import Path
import sys
import random
from datetime import date, timedelta

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from db import engine
from sqlalchemy import text

# Seed the random number generator for reproducibility
random.seed(42)

# Clear existing data
with engine.begin() as conn:
    conn.execute(text("""
        TRUNCATE TABLE
        shipments,
        order_items,
        orders,
        inventory,
        warehouses,
        products,
        suppliers,
        customers,
        employees,
        carriers,
        regions
        RESTART IDENTITY CASCADE
    """))

# Regions data
regions = [
    ("South India", "India"),
    ("North India", "India"),
    ("East India", "India"),
    ("West India", "India"),
    ("Central India", "India")
]

# Employees data
employees = [
    ("Raj Kumar", "Manager", 75000, "2022-01-15"),
    ("Priya Sharma", "Supervisor", 60000, "2022-03-10"),
    ("Arjun Patel", "Manager", 80000, "2021-11-05"),
    ("Sneha Reddy", "Analyst", 55000, "2023-02-20"),
    ("Vikram Singh", "Supervisor", 62000, "2021-08-18"),
    ("Anita Nair", "Manager", 78000, "2020-12-01"),
    ("Karan Gupta", "Analyst", 50000, "2023-01-12"),
    ("Meera Joshi", "Supervisor", 61000, "2022-07-25"),
    ("Rahul Verma", "Manager", 82000, "2020-05-30"),
    ("Pooja Menon", "Analyst", 52000, "2023-04-14")
]

#suppliers 

suppliers = [
    ("TechSource Ltd", "Electronics", 1, "contact@techsource.com"),
    ("FreshFoods Co", "Food", 2, "sales@freshfoods.com"),
    ("MediSupply", "Medical", 3, "info@medisupply.com"),
    ("AutoParts Hub", "Automotive", 4, "support@autoparts.com"),
    ("Textile World", "Clothing", 5, "hello@textileworld.com"),
    ("Smart Devices", "Electronics", 1, "contact@smartdevices.com"),
    ("Organic Farms", "Food", 2, "sales@organicfarms.com"),
    ("HealthPlus", "Medical", 3, "info@healthplus.com"),
    ("MotorWorks", "Automotive", 4, "support@motorworks.com"),
    ("Fashion House", "Clothing", 5, "hello@fashionhouse.com")
]

# Insert data
with engine.begin() as conn:

    # Insert regions
    for region_name, country in regions:

        conn.execute(
            text("""
                INSERT INTO regions
                (region_name, country)
                VALUES
                (:region_name, :country)
            """),
            {
                "region_name": region_name,
                "country": country
            }
        )

    # Insert employees
    for employee_name, role, salary, hire_date in employees:

        conn.execute(
            text("""
                INSERT INTO employees
                (
                    employee_name,
                    role,
                    salary,
                    hire_date
                )
                VALUES
                (
                    :employee_name,
                    :role,
                    :salary,
                    :hire_date
                )
            """),
            {
                "employee_name": employee_name,
                "role": role,
                "salary": salary,
                "hire_date": hire_date
            }
        )
    
    # Insert suppliers
    for supplier_name, supplier_type, region_id, contact_email in suppliers:
        conn.execute(
            text("""
                INSERT INTO suppliers
                (
                    supplier_name,
                    supplier_type,
                    region_id,
                    contact_email
                )
                VALUES
                (
                    :supplier_name,
                    :supplier_type,
                    :region_id,
                    :contact_email
                )
            """),
            {
                "supplier_name": supplier_name,
                "supplier_type": supplier_type,
                "region_id": region_id,
                "contact_email": contact_email
            }
        )

    # Insert customers
    cities = ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Ahmedabad", "Chennai", "Kolkata", "Surat", "Pune", "Jaipur"]
    segments = ["Regular", "Premium", "Enterprise"]
    for i in range(1, 101):
        customer_name = f"Customer {i}"
        city = random.choice(cities)
        segment = random.choices(segments, weights=[0.6, 0.3, 0.1], k=1)[0]
        conn.execute(
            text("""
                INSERT INTO customers (customer_name, city, segment)
                VALUES (:customer_name, :city, :segment)
            """),
            {
                "customer_name": customer_name,
                "city": city,
                "segment": segment
            }
        )

    # Insert carriers
    carriers = [
        ("Speedy Delivery", "Express"),
        ("National Cargo", "Freight"),
        ("Global Logistics", "Air"),
        ("Direct Way Transports", "Ground"),
        ("Oceanic Shipping", "Sea")
    ]
    for carrier_name, carrier_type in carriers:
        conn.execute(
            text("""
                INSERT INTO carriers (carrier_name, carrier_type)
                VALUES (:carrier_name, :carrier_type)
            """),
            {
                "carrier_name": carrier_name,
                "carrier_type": carrier_type
            }
        )

    # Insert products
    category_products = {
        "Electronics": [
            "Laptop Pro", "Smartphone X", "Noise Cancelling Headphones", "4K Monitor", "Wireless Charger",
            "Smart Watch v2", "Bluetooth Speaker", "External Hard Drive", "Mechanical Keyboard", "USB-C Hub"
        ],
        "Food": [
            "Organic Apples", "Whole Wheat Bread", "Premium Olive Oil", "Greek Yogurt", "Ground Coffee Beans",
            "Organic Honey", "Almond Milk", "Dark Chocolate Bar", "Green Tea", "Granola Bars"
        ],
        "Medical": [
            "Digital Thermometer", "First Aid Kit", "Surgical Masks", "Blood Pressure Monitor", "Hand Sanitizer",
            "Pain Relief Spray", "Vitamin C Tablets", "Band-Aids", "Pulse Oximeter", "Elastic Bandage"
        ],
        "Automotive": [
            "Brake Pads", "Engine Oil", "Spark Plugs", "Car Battery", "Wiper Blades",
            "Air Filter", "Tire Pressure Gauge", "LED Headlight Bulbs", "Car Shampoo", "Microfiber Towels"
        ],
        "Clothing": [
            "Cotton T-Shirt", "Denim Jacket", "Leather Belt", "Woolen Socks", "Running Shoes",
            "Athletic Shorts", "Hooded Sweatshirt", "Canvas Backpack", "Sunglasses", "Winter Gloves"
        ]
    }

    products_data = []
    supplier_counts_by_type = {}
    for s_idx, (supplier_name, supplier_type, region_id, contact_email) in enumerate(suppliers):
        supplier_id = s_idx + 1
        count = supplier_counts_by_type.get(supplier_type, 0)
        supplier_counts_by_type[supplier_type] = count + 1
        
        start_prod_idx = count * 5
        end_prod_idx = start_prod_idx + 5
        prod_names = category_products[supplier_type][start_prod_idx:end_prod_idx]
        
        for name in prod_names:
            if supplier_type in ["Electronics", "Automotive"]:
                unit_price = round(random.uniform(50.0, 1200.0), 2)
                weight_kg = round(random.uniform(0.5, 25.0), 2)
            else:
                unit_price = round(random.uniform(2.0, 80.0), 2)
                weight_kg = round(random.uniform(0.1, 5.0), 2)
                
            products_data.append({
                "supplier_id": supplier_id,
                "product_name": name,
                "category": supplier_type,
                "unit_price": unit_price,
                "weight_kg": weight_kg
            })

    product_prices = {}
    for p_idx, prod in enumerate(products_data):
        product_id = p_idx + 1
        product_prices[product_id] = prod["unit_price"]
        conn.execute(
            text("""
                INSERT INTO products (supplier_id, product_name, category, unit_price, weight_kg)
                VALUES (:supplier_id, :product_name, :category, :unit_price, :weight_kg)
            """),
            prod
        )

    # Insert warehouses
    warehouses_info = [
        ("Chennai Central WH", 1, "Chennai", 15000),
        ("Delhi NCR WH", 2, "Delhi", 25000),
        ("Kolkata Port WH", 3, "Kolkata", 18000),
        ("Mumbai Logistic WH", 4, "Mumbai", 30000),
        ("Bhopal Hub WH", 5, "Bhopal", 12000)
    ]
    # Pick 5 unique manager IDs from employees (1 to 10)
    manager_ids = random.sample(range(1, 11), 5)
    for idx, (name, region_id, city, capacity) in enumerate(warehouses_info):
        conn.execute(
            text("""
                INSERT INTO warehouses (warehouse_name, region_id, city, capacity, manager_id)
                VALUES (:warehouse_name, :region_id, :city, :capacity, :manager_id)
            """),
            {
                "warehouse_name": name,
                "region_id": region_id,
                "city": city,
                "capacity": capacity,
                "manager_id": manager_ids[idx]
            }
        )

    # Insert inventory (exactly 5 * 50 = 250 records)
    for wh_id in range(1, 6):
        for prod_id in range(1, 51):
            quantity = random.randint(50, 1000)
            reorder_level = random.randint(10, 100)
            conn.execute(
                text("""
                    INSERT INTO inventory (warehouse_id, product_id, quantity, reorder_level)
                    VALUES (:warehouse_id, :product_id, :quantity, :reorder_level)
                """),
                {
                    "warehouse_id": wh_id,
                    "product_id": prod_id,
                    "quantity": quantity,
                    "reorder_level": reorder_level
                }
            )

    # Insert orders (exactly 500 records)
    start_date = date(2025, 1, 1)
    order_statuses = ["Completed", "Processing", "Pending", "Cancelled"]
    order_status_weights = [0.75, 0.12, 0.08, 0.05]
    orders_data = []
    for i in range(1, 501):
        customer_id = random.randint(1, 100)
        random_days = random.randint(0, 500)
        order_date = start_date + timedelta(days=random_days)
        order_status = random.choices(order_statuses, weights=order_status_weights, k=1)[0]
        
        orders_data.append({
            "order_id": i,
            "customer_id": customer_id,
            "order_date": order_date,
            "order_status": order_status
        })

    for order in orders_data:
        conn.execute(
            text("""
                INSERT INTO orders (customer_id, order_date, order_status)
                VALUES (:customer_id, :order_date, :order_status)
            """),
            {
                "customer_id": order["customer_id"],
                "order_date": order["order_date"],
                "order_status": order["order_status"]
            }
        )

    # Insert order items (1500 to 2500 records)
    for order in orders_data:
        order_id = order["order_id"]
        num_items = random.randint(3, 5)
        prod_ids = random.sample(range(1, 51), num_items)
        
        for prod_id in prod_ids:
            quantity = random.randint(1, 20)
            price = product_prices[prod_id]
            conn.execute(
                text("""
                    INSERT INTO order_items (order_id, product_id, quantity, unit_price)
                    VALUES (:order_id, :product_id, :quantity, :unit_price)
                """),
                {
                    "order_id": order_id,
                    "product_id": prod_id,
                    "quantity": quantity,
                    "unit_price": price
                }
            )

    # Insert shipments (exactly 500 records, one per order)
    for order in orders_data:
        order_id = order["order_id"]
        order_date = order["order_date"]
        order_status = order["order_status"]
        
        carrier_id = random.randint(1, 5)
        warehouse_id = random.randint(1, 5)
        
        ship_delay = random.randint(1, 3)
        shipment_date = order_date + timedelta(days=ship_delay)
        
        if order_status == "Completed":
            shipment_status = random.choices(["Delivered", "Delayed"], weights=[0.85, 0.15], k=1)[0]
            if shipment_status == "Delivered":
                delivery_delay = random.randint(1, 5)
            else:
                delivery_delay = random.randint(6, 12)
            delivery_date = shipment_date + timedelta(days=delivery_delay)
        elif order_status == "Cancelled":
            shipment_status = "Cancelled"
            delivery_date = None
        else:
            shipment_status = "In Transit"
            delivery_date = None
            
        shipping_cost = round(random.uniform(10.0, 250.0), 2)
        
        conn.execute(
            text("""
                INSERT INTO shipments (order_id, carrier_id, warehouse_id, shipment_date, delivery_date, status, shipping_cost)
                VALUES (:order_id, :carrier_id, :warehouse_id, :shipment_date, :delivery_date, :status, :shipping_cost)
            """),
            {
                "order_id": order_id,
                "carrier_id": carrier_id,
                "warehouse_id": warehouse_id,
                "shipment_date": shipment_date,
                "delivery_date": delivery_date,
                "status": shipment_status,
                "shipping_cost": shipping_cost
            }
        )

print("Regions, employees, suppliers, customers, carriers, products, warehouses, inventory, orders, order_items, and shipments inserted successfully!")

# Verification
with engine.connect() as conn:

    region_count = conn.execute(text("SELECT COUNT(*) FROM regions")).scalar()
    employee_count = conn.execute(text("SELECT COUNT(*) FROM employees")).scalar()
    supplier_count = conn.execute(text("SELECT COUNT(*) FROM suppliers")).scalar()
    customer_count = conn.execute(text("SELECT COUNT(*) FROM customers")).scalar()
    carrier_count = conn.execute(text("SELECT COUNT(*) FROM carriers")).scalar()
    product_count = conn.execute(text("SELECT COUNT(*) FROM products")).scalar()
    warehouse_count = conn.execute(text("SELECT COUNT(*) FROM warehouses")).scalar()
    inventory_count = conn.execute(text("SELECT COUNT(*) FROM inventory")).scalar()
    order_count = conn.execute(text("SELECT COUNT(*) FROM orders")).scalar()
    order_item_count = conn.execute(text("SELECT COUNT(*) FROM order_items")).scalar()
    shipment_count = conn.execute(text("SELECT COUNT(*) FROM shipments")).scalar()

print(f"Regions: {region_count}")
print(f"Employees: {employee_count}")
print(f"Suppliers: {supplier_count}") 
print(f"Customers: {customer_count}")
print(f"Carriers: {carrier_count}")
print(f"Products: {product_count}")
print(f"Warehouses: {warehouse_count}")
print(f"Inventory: {inventory_count}")
print(f"Orders: {order_count}")
print(f"Order Items: {order_item_count}")
print(f"Shipments: {shipment_count}")