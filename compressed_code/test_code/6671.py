def solution():
    
    initial_employees = 852
    percent_increase = 25
    increase_amount = initial_employees * (percent_increase / 100)
    total_employees = initial_employees + increase_amount
    result = total_employees
    return result

print(solution())