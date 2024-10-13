# Cold Mail Generator

## Overview
The Cold Mail Generator is a Python-based application designed to help users create personalized cold emails for job applications. Utilizing LangChain and web scraping techniques, the application extracts job listings and generates tailored email content based on user input.

## Features
- **User Authentication**: Supports user sign-up and login, allowing users to manage their accounts and track email submissions.
- **Job Extraction**: Automatically extracts job listings from user-provided URLs using web scraping.
- **Email Generation**: Creates personalized cold emails based on extracted job data and user-defined skills.
- **Vector Database**: Used vector for portfolio mapping with desired job posters.
- **Limit on Free Attempts**: Users can submit up to 3 emails for free before being prompted to log in or sign up for premium services.
- **Database Support**: User credentials are securely stored in an SQLite database.

## Tech Stack
- **Python**: The core programming language.
- **Streamlit**: Used for creating the web application interface.
- **LangChain**: A library for working with language models and document loaders.
- **SQLite**: A lightweight database for storing user data.

## Installation
1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd cold-mail-generator
   ```

2. **Install the required packages:**
   ```bash
   pip install streamlit langchain langchain_community
   ```

3. **Create the SQLite database:**
   Run the `create_db.py` script to set up the database.
   ```bash
   python create_db.py
   ```

4. **Run the application:**
   ```bash
   streamlit run main.py
   ```

## Usage
- **Sign Up**: Create a new account by entering a username and password.
- **Login**: Use your credentials to log in and access your account.
- **Submit URL**: Enter a job listing URL to extract job information.
- **Generate Email**: The application will generate a cold email tailored to the job listing.

## Contributing
Contributions are welcome! If you have suggestions or improvements, please feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License.

## Contact
For any inquiries, please contact:
- **Name**: Tejas Sanjay Gupta
- **Email**: guptatejas86@gmail.com

```

### Notes
- Replace `<repository-url>` with the actual URL of your GitHub repository or wherever your code is hosted.
- Update the contact email at the bottom with your actual email address.
- Feel free to add more details, such as specific usage examples, screenshots, or links to documentation, as necessary.
