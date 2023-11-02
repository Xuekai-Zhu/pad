def solution():
    total_cost = 5000
    savings = 2900
    monthly_saving = 700
    months_needed = int((total_cost - savings) / monthly_saving) + 1
    result = months_needed
    return result

print(solution())