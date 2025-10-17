# Parse file XML, XSD
from lxml import etree
import xmlschema

xml_file = "catalog.xml"
xsd_file = "catalog.xsd"

def validate_xml(xml_file, xsd_file):
    # Load the XML Schema
    schema = xmlschema.XMLSchema(xsd_file)

    # Validate the XML file against the schema
    is_valid = schema.is_valid(xml_file)
    if is_valid:
        print("XML is valid.")
        return True
    else:
        print("XML is invalid.")
        # Print validation errors
        for error in schema.validate(xml_file):
            print(f" - {error}")
        return False

# Connect mySQL
import mysql.connector
from mysql.connector import Error
def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

connection = create_connection("localhost", "root", "", "xml_catalog")

# Dùng XPath để lấy dữ liệu từ categories và products.
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def insert_category(connection, category_id, category_name):
    query = f"""
    INSERT INTO categories (id, category)
    VALUES ('{category_id}', '{category_name}')
    """
    execute_query(connection, query)

def insert_product(connection, product_id, product_name, product_price, product_currency, product_stock, product_category_ref):
    query = f"""
    INSERT INTO products (id, name, currency, price, stock, categoryRef)
    VALUES ('{product_id}', '{product_name}', '{product_currency}', '{product_price}', '{product_stock}', '{product_category_ref}')
    """
    execute_query(connection, query)

def parse_and_store(xml_file, connection):
    if not validate_xml(xml_file, xsd_file):
        return
    tree = etree.parse(xml_file)
    root = tree.getroot()

    # Lấy tất cả các category
    categories = root.xpath("/catalog/categories/category")
    for category in categories:
        category_id = category.get("id")
        category_name = category.text
        insert_category(connection, category_id, category_name)
        print(f"Inserted category: {category_id}, {category_name}")

    # Lấy tất cả các product
    products = root.xpath("/catalog/products/product")
    for product in products:
        product_id = product.get("id")
        product_name = product.find("name").text
        price_element = product.find("price")
        product_price = price_element.text
        product_currency = price_element.get("currency")
        product_stock = product.find("stock").text
        category_ref = product.get("categoryRef")
        insert_product(connection, product_id, product_name, product_price, product_currency, product_stock, category_ref)
        print(f"Inserted product: {product_id}, {product_name}, {product_price}, {product_currency}, {product_stock}, {category_ref}")
    print("Data insertion completed.")

# validate_xml(xml_file, xsd_file)
parse_and_store(xml_file, connection)
