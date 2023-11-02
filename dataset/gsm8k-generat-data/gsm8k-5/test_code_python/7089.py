def solution():
    rental_cost = 150  # Zach paid $150 to rent the car
    cost_per_mile = 0.5  # Zach paid 50 cents per mile driven
    miles_driven = 620 + 744  # Zach drove a total of 620 + 744 miles

    # Calculate the total cost of the rental
    total_cost = rental_cost + (cost_per_mile * miles_driven)
    result = total_cost
    return result

print(solution())