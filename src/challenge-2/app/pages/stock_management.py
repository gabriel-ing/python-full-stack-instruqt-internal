import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text
import iris
import io

# Define admin credentials 
# !! WARNING !! 
# Never hardcode credentials in production environments. 
DUMMY_USERNAME = "admin"
DUMMY_PASSWORD = "1234"

# Initialize session state for authentication (boolean) and uploader key
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "uploader_key" not in st.session_state:
    st.session_state.uploader_key = 0


# *********************************************************************************
# ****************************** FUNCTION DEFINITIONS ******************************

## Creates log-in form to authenticate the user as an administrator
def login_form():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_btn = st.button("Log in", shortcut="Enter")

    if login_btn:
        if username == DUMMY_USERNAME and password == DUMMY_PASSWORD:
            st.session_state.authenticated = True
        else:
            st.error("Invalid username or password")



def get_stock() -> pd.DataFrame:
    '''
    Retrieve the stock table in the dataframe
    '''

    # Define connection parameters and credentials
    server = "iris"
    port = 1972
    namespace = "USER"

    ## ! Warning ! - don't hardcode credentials in production!
    username = "SuperUser"
    password = "SYS"

    # Create a connection string with the credentials
    db_url = f"iris://{username}:{password}@{server}:{port}/{namespace}"
    

    # Create SQLAlchemy Engine
    engine = create_engine(db_url)


    # SQL selection query to return all the stock
    ## !!!!CORRECT THIS LINE!!!
    # Write a SQL query to retrieve all values from the coffeeco.Inventory table
    sql =  ""

    # Query DB with SQLAlchemy engine and Pandas to return a DataFrame 
    df = pd.read_sql(sql, engine)

    # Return the dataframe
    return df

# **********************************************************************************





# --------------------------- Main Page Creation -----------------------------------

# Show login form if unauthenticated
if not st.session_state.authenticated:
    login_form()

# If authenticated, show rest of page
else:
    st.success("Authenticated")

    ## Create login button
    if st.button("Log out"):
        st.session_state.authenticated = False

    # Page headder
    st.header("View Stock")

    # Calls function to retrieve stock as a dataframe
    df = get_stock()

    # Displays current stock data
    st.dataframe(df)

