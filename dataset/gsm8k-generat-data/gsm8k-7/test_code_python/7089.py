def solution():
    rental_fee = 150
    cost_per_mile = 0.5
    monday_miles = 620
    thursday_miles = 744

    # Calculate the cost of Monday's trip
    monday_cost = monday_miles * cost_per_mile

    # Calculate the cost of Thursday's trip
    thursday_cost = thursday_miles * cost_per_mile

    # Calculate the total cost of car rental
    total_cost = rental_fee + monday_cost + thursday_cost
    result = total_cost
    return result

print(solution())