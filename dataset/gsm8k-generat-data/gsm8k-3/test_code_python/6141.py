def solution():
    """The cost of filling a car fuel tank is $45, and this can take you 500 miles before refilling. Mallory was going to her grammy's house, 2000 miles away. If she used 3/5 times as much money on food as she spent on filling the car fuel tank for the whole journey, calculate the total amount of money she used."""
    # Define the cost of filling a car fuel tank and the distance it can cover
    FUEL_COST = 45
    FUEL_DISTANCE = 500

    # Define the distance Mallory traveled
    distance_traveled = 2000

    # Calculate the number of times Mallory needed to refill the fuel tank
    num_refills = distance_traveled // FUEL_DISTANCE

    # Calculate the total cost of filling the fuel tank for the whole journey
    fuel_cost_total = num_refills * FUEL_COST

    # Calculate the amount of money Mallory used on food
    food_cost = (3/5) * fuel_cost_total

    # Calculate the total amount of money Mallory used
    total_cost = fuel_cost_total + food_cost

    # Display the total amount of money Mallory used
    result = total_cost
    return result

print(solution())