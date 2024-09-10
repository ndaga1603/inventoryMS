# Inventory Management System (IMS)

## Overview

The *Inventory Management System (IMS)* is a web-based solution for managing product inventory, suppliers, customers, and orders. It provides a streamlined approach to track stock levels, manage purchase and sales orders, handle customer and supplier information, and monitor inventory movements with ease.

<!-- ## Key Features

- *Product Management:* Add, update, and manage products with detailed information like price, stock level, and expiry dates.
- *Category Management:* Organize products into categories for easy searching and management.
- *Supplier Management:* Manage suppliers and their information for purchasing products.
- *Purchase Orders:* Create, track, and receive purchase orders to restock inventory.
- *Sales Orders:* Manage customer orders, including order details, status, and delivery.
- *Customer Management:* Maintain a customer database and track their orders.
- *Stock Movements:* Automatically track stock changes due to sales, purchases, and other adjustments.
- *User Roles & Permissions:* Assign roles such as Admin, Manager, and Staff with appropriate permissions for managing the system.

## Database Schema

The system uses a relational database with the following tables:

1. *Products*
2. *Categories*
3. *Suppliers*
4. *Purchase Orders*
5. *Purchase Order Items*
6. *Sales Orders*
7. *Sales Order Items*
8. *Customers*
9. *Inventory Movements*
10. *Users*
11. *User Permissions* -->

## Installation

### Setup

1. Clone the repository:

   ```bash
        git clone <https://github.com/ndaga1603/inventoryMS.git>
        cd inventoryMS
    ```

2. Set up a virtual environment:

    ```bash
        python3 -m venv venv
        source venv/bin/activate (Linux)
        venv\Scripts\activate (Windows)
    ```

3. Install the required dependencies:

   ```bash
        pip install -r requirements.txt
    ```

4. Configure the environment variables (e.g., .env file):

    ```bash
        DEBUG=True
        SECRET_KEY=your_secret_key
   ```

5. Set up the database:

    - Create a new database in PostgreSQL.

   - Migrate the database:

        ```bash
            python manage.py migrate
        ```

6. Create a superuser for admin access:

   ```bash
        python manage.py createsuperuser
   ```

7. Start the development server:

   ```bash
        python manage.py runserver
   ```

3. Open your browser and navigate to:
   <http://127.0.0.1:8000/>

## Contributing

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Commit your changes (git commit -m "Add a feature").
4. Push to the branch (git push origin feature-branch).
5. Open a pull request.

## License

This project is licensed under the MIT License.

## Contact

For any inquiries or support, please reach out to:

- *Author:* David Anderson Ndaga
- *Email:* [davidndaga1603@example.com](davidndaga1603@example.com)
