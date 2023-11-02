def solution():
    
    medical_expenses = 128
    husband_paid = medical_expenses / 2
    remaining_expenses = medical_expenses - husband_paid
    house_help_salary = 160 - remaining_expenses
    equal_split = (medical_expenses + house_help_salary) / 2
    husband_to_pay = equal_split - husband_paid
    result = husband_to_pay
    return result

print(solution())