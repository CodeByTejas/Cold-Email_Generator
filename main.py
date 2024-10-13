import streamlit as st
import sqlite3
from langchain_community.document_loaders import WebBaseLoader
from chains import Chain
from utils import clean_text

# Database functions
def get_db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row  # Allows us to access rows as dictionaries
    return conn

def insert_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    conn.commit()
    conn.close()

def get_user(username):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    conn.close()
    return user

# Custom CSS for black background
def add_custom_css():
    st.markdown("""
    <style>
    .stApp {
        background: black;
        color: red;
    }

    .iframe-container {
        position: relative;
        overflow: hidden;
        width: 100%;
        height: 500px; 
    }

    .iframe-container iframe {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        border: none;
        pointer-events: none;
    }
    </style>
    """, unsafe_allow_html=True)

# Function to check free attempts and manage login/signup prompt
def check_attempts():
    if "attempt_count" not in st.session_state:
        st.session_state.attempt_count = 0
    if "submitted_urls" not in st.session_state:
        st.session_state.submitted_urls = set()

    return st.session_state.attempt_count < 3  # Free attempts still available

# Function to prompt login/signup after limit is exceeded
def login_signup_prompt():
    st.warning("Your free limit of 3 emails has been reached. Please log in or sign up to continue.")
    if st.button("Login", key="login_button"):
        login()
    if st.button("Sign Up", key="signup_button"):
        signup()
    if st.button("Buy Paid Services", key="paid_services_button"):
        buy_services()

def login():
    st.subheader("Login")
    # Use session state to retain the input values
    username = st.text_input("Username", key="login_username", value=st.session_state.get('login_username', ''))
    password = st.text_input("Password", type='password', key="login_password", value=st.session_state.get('login_password', ''))

    if st.button("Login", key="login_submit_button"):
        if username in st.session_state.users and st.session_state.users[username] == password:
            st.session_state.logged_in = True
            st.success("Login successful!")
        else:
            st.error("Invalid username or password.")

def signup():
    st.subheader("Sign Up")
    # Use session state to retain the input values
    new_username = st.text_input("New Username", key="signup_username", value=st.session_state.get('signup_username', ''))
    new_password = st.text_input("New Password", type='password', key="signup_password", value=st.session_state.get('signup_password', ''))

    if st.button("Sign Up", key="signup_submit_button"):
        if new_username and new_password:
            if new_username not in st.session_state.users:
                st.session_state.users[new_username] = new_password
                st.session_state.signup_username = new_username  
                st.session_state.signup_password = new_password  
                st.success("Account created successfully!")
            else:
                st.error("Username already exists. Please choose another.")
        else:
            st.error("Please fill out all fields.")


def buy_services():
    st.subheader("Purchase Paid Services")
    st.write("To access premium features, please provide your payment details.")
    if st.button("Proceed to Payment"):
        st.success("Payment processed successfully! You now have access to premium features.")

def create_streamlit_app(llm, clean_text):
    from portfolio import Portfolio  # Local import to avoid circular import

    st.title("📧 Cold Mail Generator")
    portfolio = Portfolio()  # Instantiate Portfolio here

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    
    if not st.session_state.logged_in and check_attempts():
        url_input = st.text_input("Enter a URL:", value="")
        if st.button("Submit") and url_input:
            if url_input not in st.session_state.submitted_urls:
                st.session_state.attempt_count += 1
                st.session_state.submitted_urls.add(url_input)

            try:
                loader = WebBaseLoader([url_input])
                data = clean_text(loader.load().pop().page_content)
                portfolio.load_portfolio()
                jobs = llm.extract_jobs(data)
                for job in jobs:
                    skills = job.get('skills', [])
                    links = portfolio.query_links(skills)
                    email = llm.write_mail(job, links)
                    st.code(email, language='markdown')
            except Exception as e:
                st.error(f"An Error Occurred: {e}")
    else:
        login_signup_prompt()

    st.markdown("""
        <div class="iframe-container">
            <iframe src='https://my.spline.design/photorealearth-2fcac0dc42297970c27df48caff0054f/' 
            frameborder='0' width='100%' height='100%'></iframe>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    chain = Chain()
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    
    if "users" not in st.session_state:
        st.session_state.users = {}

    add_custom_css()
    create_streamlit_app(chain, clean_text)
