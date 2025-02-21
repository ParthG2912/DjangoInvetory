# Install Django
```bash
pip install django
```
# Verify Django Installation
```bash
python -m django --version
```

# Create a Django Project
```bash
mkdir djangoInventory  
cd djangoInventory  
django-admin startproject mysite .
```

# Start Developement Server
```bash
python manage.py runserver
```
By default, the server runs at http://127.0.0.1:8000/.

# Create Inventory App
```bash
python manage.py startapp inventory
```