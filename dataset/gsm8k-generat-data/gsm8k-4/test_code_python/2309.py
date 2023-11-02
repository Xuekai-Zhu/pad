def solution():
    """A new factory opens up and hires 20 people to make t-shirts. Each person makes on average 20 shirts per day during their 8-hour shift. The employees each get paid $12 an hour plus $5 per shirt they make. The company sells shirts for $35 each. Nonemployee expenses come out to $1000 a day. How much does the company make in profits per day?"""
    # Define the number of employees and the number of shirts produced per day
    num_employees = 20
    num_shirts_per_employee = 20
    num_shirts = num_employees * num_shirts_per_employee
    
    # Calculate the total cost of paying employees
    employee_pay = num_employees * 8 * 12
    
    # Calculate the total cost of paying employees per shirt
    employee_pay_per_shirt = employee_pay / num_shirts + 5
    
    # Calculate the total revenue from selling shirts
    revenue = num_shirts * 35
    
    # Calculate the total expenses including non-employee expenses and employee pay
    expenses = revenue * employee_pay_per_shirt + 1000
    
    # Calculate the daily profit
    profit = revenue - expenses
    
    result = profit
    return result

print(solution())