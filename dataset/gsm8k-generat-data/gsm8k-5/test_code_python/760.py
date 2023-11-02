def solution():
    guests = 30  # Susan is planning on having 30 guests
    servings_per_recipe = 2  # Each recipe makes 2 servings
    potatoes_per_recipe = 4  # Each recipe requires 4 potatoes
    salt_per_recipe = 1  # Each recipe requires 1 teaspoon of salt
    cost_per_potato = 0.1  # A potato costs $0.10
    cost_per_salt_container = 2  # A container of salt costs $2
    teaspoons_per_salt_container = 5  # A container of salt has 5 teaspoons

    # Calculate the number of recipes Susan needs to make
    recipes = (guests * servings_per_recipe) / servings_per_recipe

    # Calculate the number of potatoes and salt needed
    potatoes_needed = recipes * potatoes_per_recipe
    salt_needed = recipes * salt_per_recipe

    # Calculate the total cost of potatoes and salt
    cost_of_potatoes = potatoes_needed * cost_per_potato
    cost_of_salt_containers = (salt_needed / teaspoons_per_salt_container) * cost_per_salt_container
    total_cost = cost_of_potatoes + cost_of_salt_containers
    result = total_cost
    return result

print(solution())