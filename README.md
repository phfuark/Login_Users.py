# Python User Registration and Login System  

## Description
This Python script implements a basic user registration and login system. It stores user credentials in a CSV file for simplicity. 

## Features 📌
1️⃣ **User Registration:** Allows new users to create accounts.
2️⃣ **User Authentication:** Verifies user credentials against stored data.
3️⃣ **Persistent Data:** Stores user information in a CSV file.

## How to Use 🤔
1. **Save the script:** Save the code as a Python file (e.g., `user_system.py`).
2. **Run the script:** Execute the script from your terminal using `python user_system.py`.
3. **Follow the prompts:** The script will provide a menu with options for login and registration.

## Code Structure </>
* **`initialize_csv()`:** Creates the CSV file if it doesn't exist.
* **`register()`:** Adds a new user to the CSV.
* **`login()`:** Authenticates a user based on provided credentials.
* **`main()`:** The main function that handles the user interface.

## Dependencies 📚
📖 **csv:** For reading and writing CSV files ().
📖 **os:** For checking file existence ().
