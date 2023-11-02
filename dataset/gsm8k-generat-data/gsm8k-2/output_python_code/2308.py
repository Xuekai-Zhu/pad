def solution():
    """A new factory opens up and hires 20 people to make t-shirts. Each person makes on average 20 shirts per day during their 8-hour shift. The employees each get paid $12 an hour plus $5 per shirt they make. The company sells shirts for $35 each. Nonemployee expenses come out to $1000 a day. How much does the company make in profits per day?"""
    employee_count = 20
    shirts_per_person = 20
    work_hours = 8
    employee_pay_per_hour = 12
    employee_pay_per_shirt = 5
    shirt_price = 35
    non_employee_expenses = 1000
    
    # Calculate total employee expenses
    employee_expenses_per_day = (employee_count * employee_pay_per_hour * work_hours) + (employee_count * shirts_per_person * employee_pay_per_shirt)
    
    # Calculate total revenue
    total_shirts_per_day = employee_count * shirts_per_person
    revenue_per_day = total_shirts_per_day * shirt_price
    
    # Calculate profits
    profits_per_day = revenue_per_day - employee_expenses_per_day - non_employee_expenses
    
    result = profits_per_day
    return result

print(solution())