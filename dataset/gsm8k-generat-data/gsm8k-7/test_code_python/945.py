def solution():
    num_coffees_per_day = 2
    cost_per_coffee = 2
    num_days_in_April = 30

    # Calculate the total number of coffees that Jon will buy in April
    total_coffees = num_coffees_per_day * num_days_in_April

    # Calculate the total cost of all coffees that Jon will buy in April
    total_cost = total_coffees * cost_per_coffee
    result = total_cost
    return result

print(solution())