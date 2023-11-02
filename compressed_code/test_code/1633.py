def solution():
    
    salary = 2000
    tax = 0.2 * salary
    insurance = 0.05 * salary
    remaining_salary = salary - tax - insurance
    utility_bills = 0.25 * remaining_salary
    total_expenses = tax + insurance + utility_bills
    remaining_money = salary - total_expenses
    result = remaining_money
    return result

print(solution())