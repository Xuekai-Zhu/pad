def solution():
    """Mark just got a new puppy that cost $10. He also bought enough food for 3 weeks. He knows the puppy eats 1/3 cup of food a day. A bag of food with 3.5 cups costs $2. How much did all of this cost him?"""
    # Define the cost of the puppy and the food bag
    puppy_cost = 10
    food_bag_cost = 2

    # Define the amount of food the puppy eats per day and the number of weeks
    daily_food = 1/3
    weeks = 3

    # Calculate the total amount of food needed for 3 weeks
    total_food = daily_food * 7 * weeks

    # Calculate the total number of food bags needed
    total_bags = total_food / 3.5

    # Calculate the total cost of the food
    total_food_cost = total_bags * food_bag_cost

    # Calculate the total cost of getting the puppy and its food
    total_cost = puppy_cost + total_food_cost

    # Return the result
    return total_cost

print(solution())