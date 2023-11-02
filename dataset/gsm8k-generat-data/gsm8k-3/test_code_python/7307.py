def solution():
    """Mark just got a new puppy that cost $10. He also bought enough food for 3 weeks. He knows the puppy eats 1/3 cup of food a day. A bag of food with 3.5 cups costs $2. How much did all of this cost him?"""
    # Define the cost of the puppy and the amount of food needed per day
    PUPPY_COST = 10
    FOOD_PER_DAY = 1/3

    # Calculate the total amount of food needed for 3 weeks
    food_needed = 3 * 7 * FOOD_PER_DAY

    # Calculate the number of bags of food needed
    bags_needed = food_needed / 3.5

    # Calculate the total cost of the food
    food_cost = bags_needed * 2

    # Calculate the total cost of the puppy and food
    total_cost = PUPPY_COST + food_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())