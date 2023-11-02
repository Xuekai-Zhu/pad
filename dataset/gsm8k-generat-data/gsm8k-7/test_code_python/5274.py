def solution():
    miles_per_gallon = 50
    miles_per_day = 75
    cost_per_gallon = 3.0
    num_days = 10

    # Calculate the total number of gallons Tom will need during the period
    total_gallons = miles_per_day * num_days / miles_per_gallon

    # Calculate the total cost of gas Tom will need to pay for
    total_cost = total_gallons * cost_per_gallon
    result = total_cost
    return result

print(solution())