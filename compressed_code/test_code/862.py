def solution():
    
    initial_employees = 852
    percent_increase = 25
    additional_employees = initial_employees * (percent_increase / 100)
    total_employees = initial_employees + additional_employees
    result = total_employees
    return result

print(solution())