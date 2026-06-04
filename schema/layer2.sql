CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    supplier_id INTEGER NOT NULL,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    unit_price NUMERIC(10,2) NOT NULL CHECK (unit_price > 0),
    weight_kg NUMERIC(8,2) NOT NULL CHECK (weight_kg > 0),
    is_active BOOLEAN DEFAULT TRUE,

    CONSTRAINT fk_product_supplier
        FOREIGN KEY (supplier_id)
        REFERENCES suppliers(supplier_id)
);

CREATE TABLE warehouses (
    warehouse_id SERIAL PRIMARY KEY,
    warehouse_name VARCHAR(100) UNIQUE NOT NULL,
    region_id INTEGER NOT NULL,
    city VARCHAR(100) NOT NULL,
    capacity INTEGER NOT NULL CHECK (capacity > 0),
    manager_id INTEGER UNIQUE NOT NULL,

    CONSTRAINT fk_warehouse_region
        FOREIGN KEY (region_id)
        REFERENCES regions(region_id),

    CONSTRAINT fk_warehouse_manager
        FOREIGN KEY (manager_id)
        REFERENCES employees(employee_id)
);