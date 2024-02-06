import streamlit as st
import mysql.connector
from mysql.connector import Error

def create_server_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="admin",
            passwd="test123",
            database="alieat"
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")

connection = create_server_connection("host_name", "username", "password", "db_name")

st.title("Call Center Management System")

phone_number = st.text_input("Enter Customer's Phone Number:")

if phone_number:
    user_check_query = f"SELECT * FROM customers WHERE phone_no = '{phone_number}'"
    user_exists = execute_read_query(connection, user_check_query)

    if user_exists:
        st.write("Customer Found:")
        st.write(user_exists)

        past_orders_query = f"SELECT * FROM orders WHERE customer_phone_no = '{phone_number}'"
        past_orders = execute_read_query(connection, past_orders_query)
        if past_orders:
            st.write("Past Orders:")
            for order in past_orders:
                st.write(order)
        else:
            st.write("No past orders found.")

        new_order = st.text_area("Enter New Order Details:")
        if st.button("Save New Order"):
            st.write("New Order Saved")
    else:
        st.write("Customer not found. Please enter customer details.")

        name = st.text_input("Name:")
        nic_no = st.text_input("NIC Number:")
        address = st.text_input("Address:")
        if st.button("Save Customer"):
            st.write("Customer Saved")

