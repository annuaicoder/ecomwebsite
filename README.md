🛒 EcomWebsite
EcomWebsite is a full-stack e-commerce platform combining a responsive HTML/CSS/JavaScript frontend with a robust Django backend. It offers features like product browsing, shopping cart management, user authentication, and order processing.

📂 Table of Contents
Features

Tech Stack

Project Structure

Installation

Usage

Screenshots

Contributing

License

Contact

✨ Features
User Authentication: Secure registration and login system.

Product Catalog: Browse and search products with detailed descriptions.

Shopping Cart: Add, update, and remove items from the cart.

Order Management: Track and manage orders efficiently.

Responsive Design: Optimized for various devices and screen sizes.
GitHub
+2
GitHub
+2
GitHub
+2

🛠️ Tech Stack
Frontend: HTML, CSS, JavaScript

Backend: Python, Django

Database: SQLite (default), can be configured for PostgreSQL or MySQL

Authentication: Django's built-in authentication system
GitHub
+3
GeeksforGeeks
+3
GitHub
+3

🗂️ Project Structure
bash
Copy
Edit
ecomwebsite/
├── static/                 # Static files (CSS, JS, images)
├── templates/              # HTML templates
├── ecomwebsite/            # Django project settings
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── shop/                   # Django app for shop functionality
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── db.sqlite3              # SQLite database
├── manage.py               # Django's command-line utility
└── README.md
🚀 Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/annuaicoder/ecomwebsite.git
cd ecomwebsite
Create a virtual environment:

bash
Copy
Edit
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Apply migrations:

bash
Copy
Edit
python manage.py migrate
Create a superuser:

bash
Copy
Edit
python manage.py createsuperuser
Run the development server:

bash
Copy
Edit
python manage.py runserver
Access the application:
Open your browser and navigate to http://127.0.0.1:8000/

📖 Usage
Home Page: Displays featured products and categories.

Product Detail: View detailed information about a product.

Cart: Add or remove products, and proceed to checkout.

Admin Panel: Manage products, orders, and users via Django's admin interface at http://127.0.0.1:8000/admin/.
GitHub

🖼️ Screenshots
![Splash 1](https://www.coderio.com/wp-content/uploads/2024/12/Django-The-Python-Web-Framework.jpg)
![Splash 2](https://bigdataanalyticsnews.com/wp-content/uploads/2023/12/Global-Ecommerce.jpg)

🤝 Contributing
Contributions are welcome! To contribute:

Fork the repository.

Create a new branch:

bash
Copy
Edit
git checkout -b feature/your-feature-name
Make your changes and commit them:

bash
Copy
Edit
git commit -m "Add your message here"
Push to your forked repository:

bash
Copy
Edit
git push origin feature/your-feature-name
Open a Pull Request: Describe your changes and submit the PR for review.

📄 License
This project is licensed under the MIT License.

📬 Contact
For questions or feedback:

GitHub: annuaicoder