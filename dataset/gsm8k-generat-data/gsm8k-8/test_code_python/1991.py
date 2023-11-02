def solution():
    # Calculate the total cost of tickets and meals
    ticket_cost = 55
    meal_cost = 25
    total_cost = ticket_cost + meal_cost

    # Calculate the total cost of gas
    distance = 165
    mpg = 30
    price_per_gallon = 3
    gallons_needed = distance / mpg
    gas_cost = gallons_needed * price_per_gallon

    # Calculate the total cost of the trip
    total_trip_cost = total_cost + gas_cost + 10  # adding parking cost

    # Calculate how much more Sally needs to save up
    starting_savings = 28
    remaining_cost = total_trip_cost - starting_savings
    result = remaining_cost
    return result

print(solution())