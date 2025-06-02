from django.contrib import admin
from .models import Products, Order, Profile

# 👇 Admin site is used to manage models via Django's built-in UI.
# Below, we register each model so they appear in the admin dashboard.

# 🧾 Registering the Order model:
# This allows admin users to view, add, edit, and delete orders through the admin interface.
admin.site.register(Order)

# 🛍️ Registering the Products model:
# Makes all product entries manageable from the Django admin.
# Useful for updating inventory, pricing, descriptions, etc.
admin.site.register(Products)

# 🙍‍♂️ Registering the Profile model:
# Extends the default user model with custom fields (like address, phone, etc.).
# Allows admin to manage user-related data conveniently.
admin.site.register(Profile)
