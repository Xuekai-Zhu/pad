def solution():
    fill_time = 50  # The pool normally takes 50 hours to fill
    flow_rate = 100  # The hose runs at 100 gallons per hour
    total_gallons = fill_time * flow_rate  # Calculate the total number of gallons required to fill the pool
    cost_per_gallon = 0.001  # Water costs 1 cent for 10 gallons, so 1 gallon costs 0.1 cent or 0.001 dollar

    # Calculate the total cost to fill the pool
    total_cost = total_gallons * cost_per_gallon
    result = total_cost
    return result

print(solution())