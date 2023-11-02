def solution():
    """Susan wants to throw a party for her mom. She is planning on having 30 guests. For dinner she is making a recipe that makes 2 servings each. Each batch of the recipe calls for 4 potatoes and 1 teaspoon of salt. A potato costs $.10 and a container of salt costs $2 at the supermarket. If each container of salt has 5 teaspoons, how much money will Susan spend on food?"""
    # Define the number of guests and servings
    guests = 30
    servings_per_batch = 2

    # Calculate the total number of batches needed
    batches = guests / servings_per_batch

    # Calculate the amount of potatoes needed
    potatoes_per_batch = 4
    total_potatoes = batches * potatoes_per_batch

    # Calculate the cost of the potatoes
    potato_cost = total_potatoes * 0.1

    # Calculate the amount of salt needed
    salt_per_batch = 1 / 5
    total_salt = batches * salt_per_batch

    # Calculate the cost of the salt
    salt_cost = 2

    # Calculate the total cost of the food
    total_cost = potato_cost + salt_cost

    result = total_cost
    return result

print(solution())