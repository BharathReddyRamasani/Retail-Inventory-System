# 🛍️ Retail Management System CLI

## 📌 Problem Statement

This project demonstrates how to build a **real-world Retail Inventory Management System** using Python and Supabase/Postgres. It simulates actual retail operations like managing products, customers, orders, payments, and generating critical business reports through a clean, command-driven interface.

---

## 🚀 Features

### 👕 Product Management
-   **Add new products** with SKU, price, stock levels, and category.
-   **Update, list, and view** product details.
-   **Check for low-stock products** below a specified threshold.
-   **Restock** products to update inventory counts.

### 👥 Customer Management
-   **Add, update, delete, and list** customer profiles.
-   **Search for customers** by their email or city for quick lookups.

### 🛒 Order Management
-   **Create orders** with multiple products and quantities in a single command.
-   **Show detailed order information**, including customer data and line items.
-   **Cancel orders**, which automatically restocks the items and processes a refund if payment was made.

### 💳 Payment Management
-   **Process payments** for orders via multiple methods: `Cash`, `Card`, or `UPI`.
-   **Refund payments** automatically when an associated order is cancelled.
-   Handles `datetime` serialization for clean JSON output.

### 📊 Reporting
-   **Top-selling products**: Identify which products are most popular.
-   **Total revenue last month**: Get a snapshot of financial performance.
-   **Orders per customer**: Analyze customer purchasing habits.
-   **Frequent customers**: Identify and reward loyal customers based on their order count.

### 🗄️ Supabase/Postgres Database
-   Utilizes a **persistent relational database** for storing all product, customer, order, and payment data.
-   Ensures data integrity with foreign key constraints and relationships.

### 🖥️ Command-Line Interface (CLI)
-   A **fully interactive CLI** built with Python's `argparse`.
-   Provides clear commands, arguments, and help messages for easy interaction without a graphical user interface.

---

## 🛠️ Technology Stack

-   **Backend**: Python 3.8+
-   **Database**: Supabase (PostgreSQL)
-   **CLI Framework**: `argparse` (Python Standard Library)
-   **Dependencies**: `supabase-py`, `python-dotenv`

---

## 🚀 Getting Started

### 1. Prerequisites
-   Git, Python 3.8+, and a free [Supabase](https://supabase.com/) account.

### 2. Installation & Setup
1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd retail-system
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv && source venv/bin/activate
    # On Windows: venv\Scripts\activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install supabase python-dotenv
    ```
4.  **Configure your `.env` file** in the project root with your Supabase URL and Key.
5.  **Run the `schema.sql` script** in the Supabase SQL Editor to set up your database tables.

---