# Supply Chain Analytics Database V2

## Business Overview

This database models a supply chain and logistics company. It tracks suppliers, products, warehouses, inventory, customers, orders, shipments, carriers, and employees.

---

## Entity Relationship Overview

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

Order
→ Order Items

Product
→ Order Items

Order
→ Shipments

Carrier
→ Shipments

Warehouse
→ Shipments

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

Stores product suppliers.

### Columns

| Column        | Description                |
| ------------- | -------------------------- |
| supplier_id   | Unique supplier identifier |
| supplier_name | Supplier name              |
| supplier_type | Supplier category          |
| region_id     | Supplier region            |

### Relationships

* Belongs to one region.
* Supplies many products.

---

## 4. products

### Purpose

Stores products sold by the company.

### Columns

| Column       | Description               |
| ------------ | ------------------------- |
| product_id   | Unique product identifier |
| supplier_id  | Product supplier          |
| product_name | Product name              |
| category     | Product category          |
| unit_price   | Product price             |
| weight_kg    | Product weight            |
| is_active    | Product status            |

### Relationships

* Belongs to one supplier.
* Appears in many order items.
* Appears in inventory.

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
| capacity       | Maximum capacity            |
| manager_id     | Warehouse manager           |

### Relationships

* Belongs to one region.
* Managed by one employee.
* Stores inventory.
* Ships orders.

---

## 6. inventory

### Purpose

Tracks stock levels.

### Columns

| Column         | Description             |
| -------------- | ----------------------- |
| inventory_id   | Unique inventory record |
| warehouse_id   | Warehouse storing stock |
| product_id     | Product being stored    |
| stock_quantity | Available stock         |
| reorder_level  | Minimum safe stock      |
| last_updated   | Last update timestamp   |

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
| created_at    | Registration date          |

### Relationships

* Can place many orders.

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
| order_status | Order status            |
| total_amount | Total order value       |

### Relationships

* Belongs to one customer.
* Contains many order items.
* May have shipments.

---

## 9. order_items

### Purpose

Stores products within an order.

### Columns

| Column        | Description                    |
| ------------- | ------------------------------ |
| order_item_id | Unique order item identifier   |
| order_id      | Parent order                   |
| product_id    | Product ordered                |
| quantity      | Quantity ordered               |
| unit_price    | Product price at purchase time |

### Relationships

* Links orders and products.

---

## 10. carriers

### Purpose

Stores shipping carriers.

### Columns

| Column       | Description               |
| ------------ | ------------------------- |
| carrier_id   | Unique carrier identifier |
| carrier_name | Carrier name              |
| carrier_type | Carrier type              |

### Relationships

* Handles shipments.

---

## 11. shipments

### Purpose

Tracks delivery operations.

### Columns

| Column        | Description                |
| ------------- | -------------------------- |
| shipment_id   | Unique shipment identifier |
| order_id      | Associated order           |
| carrier_id    | Carrier used               |
| warehouse_id  | Origin warehouse           |
| shipment_date | Date shipped               |
| delivery_date | Date delivered             |
| status        | Shipment status            |
| delay_days    | Delivery delay             |
| shipping_cost | Shipping cost              |

### Relationships

* Belongs to an order.
* Uses a carrier.
* Originates from a warehouse.


## Foreign Keys

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

order_items.order_id
→ orders.order_id

order_items.product_id
→ products.product_id

shipments.order_id
→ orders.order_id

shipments.carrier_id
→ carriers.carrier_id

shipments.warehouse_id
→ warehouses.warehouse_id