#expense_tracker / admin.py

from django.contrib import admin
from .models import Expense

admin.site.register(Expense)
