CREATE TABLE employee_territories(
                               employeeID  INTEGER,
                               territoryID INTEGER not null
                               );
CREATE TABLE orders(
                         orderID        INT PRIMARY KEY,
                         customerID     CHAR(5),
                         employeeID     INTEGER,
                         orderDate      date,
                         requiredDate   date,
                         shippedDate    VARCHAR(255),
                         shipVia        INTEGER,
                         freight        FLOAT,
                         shipName       VARCHAR(255),
                         shipAddress    VARCHAR(255),
                         shipCity       VARCHAR(255),
                         shipRegion     VARCHAR(255),
                         shipPostalCode VARCHAR(255),
                         shipCountry    VARCHAR(255)
                        );
CREATE TABLE employees(
                              employeeID      INT PRIMARY KEY,
                              lastName        VARCHAR(255),
                              firstName       VARCHAR(255) ,
                              title           VARCHAR(255),
                              titleOfCourtesy VARCHAR(255),
                              birthDate       DATE,
                              hireDate        DATE,
                              address         VARCHAR(255),
                              city            VARCHAR(255),
                              region          VARCHAR(255),
                              postalCode      VARCHAR(255),
                              country         VARCHAR(255),
                              homePhone       VARCHAR(255),
                              extension       INTEGER,
                              photo           TEXT,
                              notes           TEXT,
                              reportsTo       TEXT,
                              photoPath       TEXT
                              );
CREATE TABLE regions(
                          regionID          INT PRIMARY KEY,
                          regionDescription VARCHAR(255)
                         );
CREATE TABLE categories(
                            categoryID   INTEGER,
                            categoryName VARCHAR(255),
                            description  VARCHAR(255),
                            picture      TEXT
                           );
CREATE TABLE order_details(
                                orderID   INTEGER,
                                productID INTEGER,
                                unitPrice FLOAT,
                                quantity  INTEGER,
                                discount  FLOAT
                                );
CREATE TABLE shippers(
                            shipperID   INTEGER,
                            companyName VARCHAR(255),
                            phone       VARCHAR(255)
                           );
CREATE TABLE products(
                            productID       INTEGER,
                            productName     VARCHAR(255),
                            supplierID      INTEGER,
                            categoryID      INTEGER,
                            quantityPerUnit VARCHAR(255),
                            unitPrice       FLOAT,
                            unitsInStock    INTEGER,
                            unitsOnOrder    INTEGER,
                            reorderLevel    INTEGER,
                            discontinued    INTEGER
                           );

CREATE TABLE suppliers(
                             supplierID   INTEGER,
                             companyName  VARCHAR(255),
                             contactName  VARCHAR(255),
                             contactTitle VARCHAR(255),
                             address      VARCHAR(255),
                             city         VARCHAR(255),
                             region       VARCHAR(255),
                             postalCode   VARCHAR(255),
                             country      VARCHAR(255),
                             phone        VARCHAR(255),
                             fax          VARCHAR(255),
                             homePage     VARCHAR(255)
                            );

CREATE TABLE customers(
                             customerID   VARCHAR(5),
                             companyName  VARCHAR(255),
                             contactName  VARCHAR(255),
                             contactTitle VARCHAR(255),
                             address      VARCHAR(255),
                             city         VARCHAR(255),
                             region       VARCHAR(255),
                             postalCode   VARCHAR(255),
                             country      VARCHAR(255),
                             phone        VARCHAR(255),
                             fax          VARCHAR(255)
                            );

CREATE TABLE territories(
                               territoryID          INTEGER,
                               territoryDescription VARCHAR(255),
                               regionID             INTEGER
                              );



COPY employee_territories FROM '/Users/dina.deifallah/Documents/sql/northwind_data/employee_territories.csv' WITH  DELIMITER ',' CSV HEADER;
COPY orders FROM '/Users/dina.deifallah/Documents/sql/northwind_data/orders.csv' WITH  DELIMITER ',' CSV HEADER;
COPY employees FROM '/Users/dina.deifallah/Documents/sql/northwind_data/employees.csv' WITH  DELIMITER ',' CSV HEADER;
COPY regions FROM '/Users/dina.deifallah/Documents/sql/northwind_data/regions.csv' WITH  DELIMITER ',' CSV HEADER;
COPY order_details FROM '/Users/dina.deifallah/Documents/sql/northwind_data/order_details.csv' WITH  DELIMITER ',' CSV HEADER;
COPY shippers FROM '/Users/dina.deifallah/Documents/sql/northwind_data/shippers.csv' WITH  DELIMITER ',' CSV HEADER;
COPY products FROM '/Users/dina.deifallah/Documents/sql/northwind_data/products.csv' WITH  DELIMITER ',' CSV HEADER;
COPY suppliers FROM '/Users/dina.deifallah/Documents/sql/northwind_data/suppliers.csv' WITH  DELIMITER ',' CSV HEADER;
COPY customers FROM '/Users/dina.deifallah/Documents/sql/northwind_data/customers.csv' WITH  DELIMITER ',' CSV HEADER;
COPY territories FROM '/Users/dina.deifallah/Documents/sql/northwind_data/territories.csv' WITH  DELIMITER ',' CSV HEADER;

------------------
-- 1. Connect to postgres
-- 2. check out the databases: \l
-- 3. connect to a database/switch databases: \c db_name
-- 4. check out tables of a database: \d 
-- 5. Check out the contents of a table: SELECT * FROM table_name; 
-- 6. run a sql-file inside psql: \i file_name.sql (or give path)
