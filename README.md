# Grocery Store Management System

A CLI-based system that is used to simulate multiple features involved in a grocery store, including:
*   Login authentication
*   Item handling operations (inserting, searching, updating, and deleting items)
*   Stock-related operations (viewing replenishment list and update stock number)

<i>Note: This is my first ever coding project where I get to explore different fundamentals of coding (and cramped every function into a single `.py` file back then [>_<]). However, do feel free to play around with the fully-functional CLI system!</i>

---

## System Architecture

The system utilizes arrays to initialise and store data internally, with standard text files used to store data outside of the program. 

*   **Language:** Python
*   **Data Storage:** Text files (`inventory.txt`, `username.txt`)
*   **Data Handling:** Arrays

---

## Core Features

*   **Role-Based Access Control (RBAC):** Distinct permission levels for Admin, Inventory checker, and Purchaser roles.
*   **Inventory Operations:** Full CRUD capabilities (Create, Read, Update, Delete) for store records.
*   **Threshold Monitoring:** Automated identification of items dropping below defined minimum quantities to trigger replenishment.
*   **Multi-Parameter Querying:** Search functionality allowing lookups by exact description, category, code range, and price range.

---

## Prerequisites for Execution
*   Python 3 environment
*   Ensure that both `inventory.txt` and `username.txt` are located in the same root directory as the Python script.

---

## Documentation
The question paper can be accessed [here](https://github.com/BengRhui/Grocery_Store_Management_System/blob/main/Assignment%20Question.docx).

