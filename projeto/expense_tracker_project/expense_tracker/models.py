# expense_tracker/models.py
from django.db import models

class Expense(models.Model):
    ALLOWED_CATEGORIES = [
        ('compras', 'Compras'),
        ('escola', 'Escola'),
        ('coisas', 'Coisas'),
    ]

    date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=100, choices=ALLOWED_CATEGORIES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return f"{self.date} - {self.category}: {self.amount}"
