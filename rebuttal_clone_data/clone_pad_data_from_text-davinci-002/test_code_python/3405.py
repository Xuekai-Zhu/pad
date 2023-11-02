def solution():
    shirts = 10
    pants = 12
    time_per_shirt = 1.5
    time_per_pants = 2
    charge_per_hour = 30
    total_cost = (shirts * time_per_shirt + pants * time_per_pants) * charge_per_hour
    result = total_cost
    return result

print(solution())