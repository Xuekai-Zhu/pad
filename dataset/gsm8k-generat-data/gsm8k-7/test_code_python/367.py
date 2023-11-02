def solution():
    emily_salary = 1000000
    num_employees = 10
    current_salary = 20000
    new_salary = 35000
    
    # Calculate the total cost of increasing each employee's salary
    increase_cost = (new_salary - current_salary) * num_employees
    
    # Calculate Emily's new salary after taking the cost of increasing salaries into account
    new_emily_salary = emily_salary - increase_cost
    
    result = new_emily_salary
    return result

print(solution())