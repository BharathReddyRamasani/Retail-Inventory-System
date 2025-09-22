# 📌 Retail Inventory Management System

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)  
[![Supabase](https://img.shields.io/badge/Backend-Supabase-green)](https://supabase.com/)  
[![Postgres](https://img.shields.io/badge/Database-PostgreSQL-blue)](https://www.postgresql.org/)  

---

## 📌 Problem Statement

This project demonstrates how to build a **real-world Retail Inventory Management System** using Python and Supabase/Postgres.  
It simulates actual retail operations like managing products, customers, orders, payments, and generating reports.

---

## 🚀 Features

### 👕 Product Management
- Add new products with SKU, price, stock, and category
- Update, list, and view products
- Check low-stock products and restock

### 👥 Customer Management
- Add, update, delete, and list customers
- Search customers by email or city

### 🛒 Order Management
- Create orders with multiple items
- Show order details
- Cancel orders (restores stock and refunds payment)
- Complete orders (marks as completed and processes payment)

### 💳 Payment Management
- Process payments via Cash, Card, or UPI
- Refund payments for cancelled orders
- Handles datetime serialization for JSON output

### 📊 Reporting
- Top-selling products
- Total revenue last month
- Orders per customer
- Frequent customers based on order count

### 🗄 Supabase/Postgres Database
- Persistent relational data storage for products, customers, orders, payments

### 🖥 Command-Line Interface (CLI)
- Fully menu-driven CLI for easy interaction

---

## 🛠 How to Run

```yaml
clone_repo: 
  git clone https://github.com/AnveshAnnepaga/Retail-Inventory-Management-System.git
  cd Retail-Inventory-Management-System

create_virtual_environment: |
  python -m venv venv
  # On macOS/Linux
  source venv/bin/activate
  # On Windows
  venv\Scripts\activate

install_dependencies: 
  pip install -r requirements.txt

set_env_variables: 
  Create a .env file in the project root
  Add your Supabase credentials as per .env.example

run_application: 
  python -m src.cli.main

🖥 CLI Commands:

# Products
product:
  add: python -m src.cli.main product add --name "Laptop" --sku "LP100" --price 1200 --stock 10 --category "Electronics"
  list: python -m src.cli.main product list

# Customers
customer:
  add: python -m src.cli.main customer add --name "John Doe" --email "john@example.com" --phone "1234567890" --city "NY"
  update: python -m src.cli.main customer update --customer 1 --phone "9876543210" --city "LA"
  delete: python -m src.cli.main customer delete --customer 1
  list: python -m src.cli.main customer list
  search: python -m src.cli.main customer search --email "john" --city "NY"

# Orders
order:
  create: python -m src.cli.main order create --customer 1 --item 2:3 4:1
  show: python -m src.cli.main order show --order 3
  complete: python -m src.cli.main order complete --order 3
  cancel: python -m src.cli.main order cancel --order 3

# Payments
payment:
  process: python -m src.cli.main payment process --order 3 --method UPI
  refund: python -m src.cli.main payment refund --order 3

# Reporting
report:
  top_products: python -m src.cli.main report top_products
  revenue_last_month: python -m src.cli.main report revenue_last_month
  orders_per_customer: python -m src.cli.main report orders_per_customer
  frequent_customers: python -m src.cli.main report frequent_customers --min_orders 5
