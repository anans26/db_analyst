CREATE TABLE order_items (
    order_item_id SERIAL PRIMARY KEY,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    unit_price NUMERIC(10,2) NOT NULL CHECK (unit_price > 0),

    CONSTRAINT uq_order_product
        UNIQUE (order_id, product_id),

    CONSTRAINT fk_orderitem_order
        FOREIGN KEY (order_id)
        REFERENCES orders(order_id),

    CONSTRAINT fk_orderitem_product
        FOREIGN KEY (product_id)
        REFERENCES products(product_id)
); 

CREATE TABLE shipments (
    shipment_id SERIAL PRIMARY KEY,
    order_id INTEGER NOT NULL,
    carrier_id INTEGER NOT NULL,
    warehouse_id INTEGER NOT NULL,
    shipment_date DATE NOT NULL,
    delivery_date DATE,
    status VARCHAR(30) NOT NULL,
    shipping_cost NUMERIC(10,2) NOT NULL CHECK (shipping_cost >= 0),

    CONSTRAINT chk_delivery_after_shipment
        CHECK (
            delivery_date IS NULL
            OR delivery_date >= shipment_date
        ),

    CONSTRAINT fk_shipment_order
        FOREIGN KEY (order_id)
        REFERENCES orders(order_id),

    CONSTRAINT fk_shipment_carrier
        FOREIGN KEY (carrier_id)
        REFERENCES carriers(carrier_id),

    CONSTRAINT fk_shipment_warehouse
        FOREIGN KEY (warehouse_id)
        REFERENCES warehouses(warehouse_id),

    CONSTRAINT chk_shipment_status
        CHECK (
            status IN (
                'In Transit',
                'Delivered',
                'Delayed',
                'Cancelled'
            )
        )
);