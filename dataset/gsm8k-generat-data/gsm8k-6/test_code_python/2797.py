def solution():
    # Calculate the amount spent on employee salaries
    employee_salary = (2/5) * 4000  
    
    # Calculate the remaining amount after paying employee salaries
    remaining_amount = 4000 - employee_salary  
    
    # Calculate the amount spent on delivery costs
    delivery_costs = (1/4) * remaining_amount  
    
    # Calculate the amount paid for orders done
    orders_cost = remaining_amount - delivery_costs  
    
    result = orders_cost
    return result

print(solution())