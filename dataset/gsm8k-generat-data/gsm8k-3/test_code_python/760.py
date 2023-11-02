def solution():
    """Susan wants to throw a party for her mom. She is planning on having 30 guests. For dinner she is making a recipe that makes 2 servings each. Each batch of the recipe calls for 4 potatoes and 1 teaspoon of salt. A potato costs $.10 and a container of salt costs $2 at the supermarket. If each container of salt has 5 teaspoons, how much money will Susan spend on food?"""
    # Define the number of guests and servings
    NUM_GUESTS = 30
    NUM_SERVINGS_PER_RECIPE = 2

    # Define the number of potatoes and salt needed for each recipe
    NUM_POTATOES_PER_RECIPE = 4
    NUM_SALT_PER_RECIPE = 1 / 5 # 1 container of salt has 5 teaspoons

    # Define the cost of each potato and container of salt
    POTATO_COST = 0.10
    SALT_COST = 2.00

    # Calculate the number of recipes needed
    num_recipes = (NUM_GUESTS * NUM_SERVINGS_PER_RECIPE) / 2

    # Calculate the total number of potatoes and salt needed
    total_potatoes = num_recipes * NUM_POTATOES_PER_RECIPE
    total_salt = num_recipes * NUM_SALT_PER_RECIPE

    # Calculate the total cost of the potatoes and salt
    potato_cost = total_potatoes * POTATO_COST
    salt_cost = total_salt * SALT_COST

    # Calculate the total cost of the food
    total_cost = potato_cost + salt_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())