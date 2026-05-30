# 🛍️ Mini Store Management System

A modular Command-Line Interface (CLI) application built with Python that simulates a retail store. The application supports two distinct user roles: a **Store Manager** who handles inventory and product updates, and a **Customer** who can browse products, manage a shopping cart, and check out.

---

## 🚀 Key Features

* **Role-Based Architecture:** Separate dynamic CLI flows for Store Managers and Customers.
* **Manager Authentication:** Secure access control for managers to add products, specify prices, and set inventory counts.
* **Inventory Control:** Real-time stock updates that automatically decrement when items are added to a cart and restore if an order is cancelled or removed.
* **Shopping Cart Logic:** Dynamic cart management supporting quantity updates, input validation, object reference tracking, and live total price calculations.

---

## 🛠️ Project Architecture

The codebase separates entity definitions from user interface logic:

```text
mini_store/
│
├── models.py      # Core data models (Product, Store, CartItem, Cart)
├── ui.py          # CLI layouts and business workflows (Manager, Customer menus)
└── main.py        # Application entry point
```
Component Breakdown
Product: Manages single item states (Name, Price, Stock).

Store: Holds the master inventory list and provides lookup methods.

CartItem / Cart: Tracks customer selections independently before payment processing.

## ⚙️ Requirements & Installation
This project runs completely on Python's standard library and requires no external dependencies.

Ensure you have Python 3.10 or higher installed.

Clone or download the script files into a unified project directory.
## start project
```bash
cd store_python
py main.py
```
