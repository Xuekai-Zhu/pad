def solution():
    """The cost of filling a car fuel tank is $45, and this can take you 500 miles before refilling. Mallory was going to her grammy's house, 2000 miles away. If she used 3/5 times as much money on food as she spent on filling the car fuel tank for the whole journey, calculate the total amount of money she used."""
    # Define the cost of filling the fuel tank and the number of miles it can cover
    FUEL_COST = 45
    FUEL_RANGE = 500

    # Define the distance of the trip
    TRIP_DISTANCE = 2000

    # Calculate the total number of refills needed for the trip
    refills_needed = TRIP_DISTANCE // FUEL_RANGE
    if TRIP_DISTANCE % FUEL_RANGE != 0:
        refills_needed += 1

    # Calculate the total cost of fuel for the trip
    fuel_cost_total = refills_needed * FUEL_COST

    # Calculate the amount spent on food as a fraction of the fuel cost
    food_frac = 3/5

    # Calculate the total amount spent on food
    food_cost_total = food_frac * fuel_cost_total

    # Calculate the total amount spent on the trip
    total_cost = fuel_cost_total + food_cost_total

    result = total_cost
    return result

print(solution())