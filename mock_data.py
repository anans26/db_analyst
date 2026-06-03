import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="logistics_ai",
    user="postgres",
    password="postgres",
    port=5433
)

cursor = conn.cursor()

cursor.execute("""
INSERT INTO shipments
(order_date, delivery_date, city, carrier, status, delay_days, shipping_cost, customer_segment)
VALUES
('2026-05-01','2026-05-03','Chennai','BlueDart','Delivered',0,120,'Premium'),
('2026-05-02','2026-05-06','Chennai','FedEx','Delayed',2,150,'Regular'),
('2026-05-03','2026-05-07','Bangalore','Delhivery','Delayed',1,100,'Regular'),
('2026-05-04','2026-05-05','Mumbai','BlueDart','Delivered',0,180,'Premium'),
('2026-05-05','2026-05-09','Delhi','FedEx','Delayed',3,220,'Enterprise'),
('2026-05-06','2026-05-07','Hyderabad','BlueDart','Delivered',0,110,'Regular'),
('2026-05-07','2026-05-10','Chennai','Delhivery','Delayed',2,90,'Regular'),
('2026-05-08','2026-05-09','Mumbai','FedEx','Delivered',0,160,'Premium'),
('2026-05-09','2026-05-13','Bangalore','BlueDart','Delayed',3,130,'Enterprise'),
('2026-05-10','2026-05-11','Delhi','Delhivery','Delivered',0,140,'Regular'),
('2026-05-11','2026-05-15','Chennai','FedEx','Delayed',4,200,'Enterprise'),
('2026-05-12','2026-05-13','Mumbai','BlueDart','Delivered',0,170,'Premium'),
('2026-05-13','2026-05-17','Hyderabad','FedEx','Delayed',3,125,'Regular'),
('2026-05-14','2026-05-15','Bangalore','Delhivery','Delivered',0,95,'Regular'),
('2026-05-15','2026-05-19','Delhi','BlueDart','Delayed',2,210,'Enterprise'),
('2026-05-16','2026-05-17','Chennai','FedEx','Delivered',0,175,'Premium'),
('2026-05-17','2026-05-21','Mumbai','Delhivery','Delayed',4,115,'Regular'),
('2026-05-18','2026-05-19','Hyderabad','BlueDart','Delivered',0,105,'Regular'),
('2026-05-19','2026-05-23','Bangalore','FedEx','Delayed',3,190,'Enterprise'),
('2026-05-20','2026-05-21','Delhi','Delhivery','Delivered',0,135,'Regular'),
('2026-05-21','2026-05-24','Chennai','BlueDart','Delayed',2,150,'Premium'),
('2026-05-22','2026-05-23','Mumbai','FedEx','Delivered',0,165,'Premium'),
('2026-05-23','2026-05-27','Hyderabad','Delhivery','Delayed',3,120,'Regular'),
('2026-05-24','2026-05-25','Bangalore','BlueDart','Delivered',0,145,'Enterprise'),
('2026-05-25','2026-05-29','Delhi','FedEx','Delayed',4,230,'Enterprise');
""")

conn.commit()

print("Data inserted successfully!")

cursor.close()
conn.close()    