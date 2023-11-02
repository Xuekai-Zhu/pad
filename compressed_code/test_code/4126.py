def solution():
    
    salary = 60000
    monthly_savings = 1000
    ring_cost = 2 * (salary/12)
    months_needed = ring_cost/monthly_savings
    result = months_needed
    return result

print(solution())