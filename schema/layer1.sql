CREATE TABLE regions (
    region_id SERIAL PRIMARY KEY,
    region_name VARCHAR(100) UNIQUE NOT NULL,
    country VARCHAR(100) NOT NULL
);

CREATE TABLE employees (
    employee_id SERIAL PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL,
    role VARCHAR(50) NOT NULL,
    salary NUMERIC(10,2) NOT NULL CHECK (salary > 0),
    hire_date DATE NOT NULL
);

CREATE TABLE suppliers (
    supplier_id SERIAL PRIMARY KEY,
    supplier_name VARCHAR(100) UNIQUE NOT NULL,
    supplier_type VARCHAR(50) NOT NULL,
    region_id INTEGER NOT NULL,
    contact_email VARCHAR(255) UNIQUE NOT NULL,

    CONSTRAINT fk_supplier_region
        FOREIGN KEY (region_id)
        REFERENCES regions(region_id)
);

CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    city VARCHAR(100) NOT NULL,

    segment VARCHAR(50) NOT NULL
    CHECK (
        segment IN (
            'Regular',
            'Premium',
            'Enterprise'
        )
    ),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE carriers (
    carrier_id SERIAL PRIMARY KEY,
    carrier_name VARCHAR(100) UNIQUE NOT NULL,
    carrier_type VARCHAR(50) NOT NULL
);
