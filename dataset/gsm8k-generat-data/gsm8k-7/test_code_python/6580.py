def solution():
    pool_fill_time = 50
    hose_rate = 100
    cost_per_gallon = 0.001  # 1 cent for 10 gallons

    # Calculate the total number of gallons required to fill the pool
    total_gallons = pool_fill_time * hose_rate

    # Calculate the total cost of filling the pool
    total_cost = total_gallons * cost_per_gallon
    result = total_cost
    return result

print(solution())