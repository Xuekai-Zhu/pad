def solution():
     """Mrs. Snyder used to spend 40% of her monthly income on rent and utilities. Her salary was recently increased by $600 so now her rent and utilities only amount to 25% of her monthly income. How much was her previous monthly income?"""
     percentage_spent = 40
     monthly_increase = 600
     current_percentage = 25
     previous_income = (monthly_increase / (current_percentage - percentage_spent)) * 100
     result = previous_income
     return result

print(solution())