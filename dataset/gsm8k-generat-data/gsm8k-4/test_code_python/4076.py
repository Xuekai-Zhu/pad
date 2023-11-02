def solution():
    """There are 50 goldfish in the pond. Each goldfish eats 1.5 ounces of food per day. 20% of the goldfish need to eat special food that costs $3 an ounce. How much does it cost to feed these fish?"""
    # Define the number of goldfish and the amount of food they eat
    num_goldfish = 50
    food_per_goldfish = 1.5

    # Calculate the total amount of food needed per day
    total_food = num_goldfish * food_per_goldfish

    # Calculate the number of goldfish that need special food
    num_special_food = int(num_goldfish * 0.2)

    # Calculate the cost of the special food for one day
    special_food_cost = num_special_food * food_per_goldfish * 3

    # Return the cost of special food for one day
    result = special_food_cost
    return result

print(solution())