def solution():
    """A new factory opens up and hires 20 people to make t-shirts. Each person makes on average 20 shirts per day during their 8-hour shift. The employees each get paid $12 an hour plus $5 per shirt they make. The company sells shirts for $35 each. Nonemployee expenses come out to $1000 a day. How much does the company make in profits per day?"""
    num_employees = 20
    shirts_per_employee = 20
    num_hours_per_shift = 8
    employee_wage_per_hour = 12
    wage_per_shirt = 5
    shirt_price = 35
    nonemployee_expenses = 1000
    
    total_num_shirts = num_employees * shirts_per_employee * num_hours_per_shift
    labor_cost = (num_hours_per_shift * employee_wage_per_hour * num_employees) + (wage_per_shirt * total_num_shirts)
    revenue = total_num_shirts * shirt_price
    profits = revenue - (labor_cost + nonemployee_expenses)
    result = profits
    
    return result

print(solution())