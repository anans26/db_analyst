# Supply Chain Analytics Database V2

## Business Overview

This database models a supply chain and logistics company. It tracks suppliers, products, warehouses, inventory, customers, orders, carriers, and employees.

The system is designed to support:

* Inventory Management
* Order Tracking
* Warehouse Operations
* Supplier Analysis
* Customer Analytics
* Logistics Reporting
* AI-Powered Natural Language Analytics

---

# Entity Relationship Overview

Region
→ Suppliers

Region
→ Warehouses

Supplier
→ Products

Warehouse
→ Inventory

Product
→ Inventory

Customer
→ Orders

Employee
→ Warehouse (Manager)

---

# Tables

## 1. regions

### Purpose

Stores geographical regions used by suppliers and warehouses.

### Columns

| Column      | Description              |
| ----------- | ------------------------ |
| region_id   | Unique region identifier |
| region_name | Name of region           |
| country     | Country name             |

### Relationships

* One region can have many suppliers.
* One region can have many warehouses.

---

## 2. employees

### Purpose

Stores employee information.

### Columns

| Column        | Description                |
| ------------- | -------------------------- |
| employee_id   | Unique employee identifier |
| employee_name | Employee name              |
| role          | Employee role              |
| salary        | Employee salary            |
| hire_date     | Date hired                 |

### Relationships

* One employee may manage a warehouse.

---

## 3. suppliers

### Purpose

Stores supplier information.

### Columns

| Column        | Description                |
| ------------- | -------------------------- |
| supplier_id   | Unique supplier identifier |
| supplier_name | Supplier name              |
| supplier_type | Supplier category          |
| region_id     | Supplier region            |
| contact_email | Supplier contact email     |

### Relationships

* Belongs to one region.
* Supplies many products.

---

## 4. products

### Purpose

Stores products supplied to the company.

### Columns

| Column       | Description                 |
| ------------ | --------------------------- |
| product_id   | Unique product identifier   |
| supplier_id  | Product supplier            |
| product_name | Product name                |
| category     | Product category            |
| unit_price   | Product price               |
| weight_kg    | Product weight              |
| is_active    | Product availability status |

### Relationships

* Belongs to one supplier.
* Appears in inventory.
* Will appear in order_items.

---

## 5. warehouses

### Purpose

Stores warehouse information.

### Columns

| Column         | Description                 |
| -------------- | --------------------------- |
| warehouse_id   | Unique warehouse identifier |
| warehouse_name | Warehouse name              |
| region_id      | Warehouse region            |
| city           | Warehouse city              |
| capacity       | Maximum storage capacity    |
| manager_id     | Warehouse manager           |

### Relationships

* Belongs to one region.
* Managed by one employee.
* Stores inventory.

---

## 6. inventory

### Purpose

Tracks stock levels across warehouses.

### Columns

| Column        | Description              |
| ------------- | ------------------------ |
| inventory_id  | Unique inventory record  |
| warehouse_id  | Warehouse storing stock  |
| product_id    | Product being stored     |
| quantity      | Available stock quantity |
| reorder_level | Minimum stock threshold  |

### Database Constraints

* quantity >= 0
* reorder_level >= 0

### Relationships

* Links products and warehouses.

---

## 7. customers

### Purpose

Stores customer information.

### Columns

| Column        | Description                |
| ------------- | -------------------------- |
| customer_id   | Unique customer identifier |
| customer_name | Customer name              |
| city          | Customer city              |
| segment       | Customer segment           |
| created_at    | Registration timestamp     |

### Relationships

* One customer can place many orders.

---

## 8. orders

### Purpose

Stores customer orders.

### Columns

| Column       | Description             |
| ------------ | ----------------------- |
| order_id     | Unique order identifier |
| customer_id  | Customer placing order  |
| order_date   | Order date              |
| order_status | Current order status    |

### Database Constraints

Valid values for order_status:

* Pending
* Processing
* Completed
* Cancelled

### Relationships

* Belongs to one customer.
* Will contain many order items.
* Will have shipment records.

### Notes

Order totals are not stored directly.

Order value is calculated from:

quantity × unit_price

stored in the order_items table.

---

## 9. carriers

### Purpose

Stores shipping carrier information.

### Columns

| Column       | Description               |
| ------------ | ------------------------- |
| carrier_id   | Unique carrier identifier |
| carrier_name | Carrier name              |
| carrier_type | Carrier category          |

### Relationships

* Will be used by shipment records.

---

# Foreign Keys

suppliers.region_id
→ regions.region_id

products.supplier_id
→ suppliers.supplier_id

warehouses.region_id
→ regions.region_id

warehouses.manager_id
→ employees.employee_id

inventory.warehouse_id
→ warehouses.warehouse_id

inventory.product_id
→ products.product_id

orders.customer_id
→ customers.customer_id

---

# Planned Layer 4 Tables

These tables will be implemented in the next phase.

## order_items

Purpose:

Stores products contained within customer orders.

Columns:

* order_item_id
* order_id
* product_id
* quantity
* unit_price

Relationships:

* Links orders and products.
* Preserves historical pricing.

---

## shipments

Purpose:

Tracks shipment and delivery operations.

Columns:

* shipment_id
* order_id
* carrier_id
* warehouse_id
* shipment_date
* delivery_date
* status
* shipping_cost

Database Constraints

Valid values for shipment status:

* In Transit
* Delivered
* Delayed
* Cancelled

Relationships:

* Belongs to an order.
* Uses a carrier.
* Originates from a warehouse.

---

# Example Analytics Questions

* Which products generate the highest revenue?
* Which suppliers contribute the most products?
* Which warehouses have the lowest inventory?
* Which products are below reorder level?
* How many orders are pending?
* Which customer segment places the most orders?
* Which region has the most suppliers?
* What is the inventory distribution across warehouses?
* Which warehouse stores the largest number of products?
* What is the average order volume by customer segment?
