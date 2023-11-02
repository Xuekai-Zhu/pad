def solution():
    
    starting_salary = 80000
    previous_salary = starting_salary * (1 + 0.4)
    current_salary = previous_salary * (1 + 0.2)
    result = current_salary
    return result

print(solution())