from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from db import engine
from sqlalchemy import text

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

print("Regions, employees, and suppliers inserted successfully!")

# Verification
with engine.connect() as conn:

    region_count = conn.execute(
        text("SELECT COUNT(*) FROM regions")
    ).scalar()

    employee_count = conn.execute(
        text("SELECT COUNT(*) FROM employees")
    ).scalar()

    supplier_count = conn.execute(
        text("SELECT COUNT(*) FROM suppliers")
    ).scalar()

print(f"Regions: {region_count}")
print(f"Employees: {employee_count}")
print(f"Suppliers: {supplier_count}") 