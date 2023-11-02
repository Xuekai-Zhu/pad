def solution():
    """There are 50 goldfish in the pond. Each goldfish eats 1.5 ounces of food per day. 20% of the goldfish need to eat special food that costs $3 an ounce. How much does it cost to feed these fish?"""
    # Define the number of goldfish and the amount of food they eat per day
    GOLDFISH_COUNT = 50
    FOOD_PER_GOLDFISH = 1.5

    # Calculate the total amount of food needed per day
    total_food = GOLDFISH_COUNT * FOOD_PER_GOLDFISH

    # Calculate the number of goldfish that need special food
    special_fish = int(GOLDFISH_COUNT * 0.2)  # 20% of the goldfish

    # Calculate the cost of feeding the special fish
    special_food_cost = special_fish * FOOD_PER_GOLDFISH * 3  # $3 per ounce

    # Display the cost of feeding the special fish
    result = special_food_cost
    return result

print(solution())