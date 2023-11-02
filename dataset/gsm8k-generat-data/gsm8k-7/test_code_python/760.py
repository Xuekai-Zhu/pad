def solution():
    num_guests = 30
    servings_per_recipe = 2
    potatoes_per_recipe = 4
    salt_per_recipe = 1
    potato_cost = 0.1
    salt_cost_per_container = 2
    teaspoons_per_container = 5

    # Calculate the number of recipes needed
    num_recipes = num_guests / servings_per_recipe

    # Calculate the number of potatoes needed
    num_potatoes = num_recipes * potatoes_per_recipe

    # Calculate the cost of all potatoes
    potato_cost_total = num_potatoes * potato_cost

    # Calculate the number of containers of salt needed
    num_salt_containers = (num_recipes * salt_per_recipe) / teaspoons_per_container

    # Calculate the cost of all salt containers
    salt_cost_total = num_salt_containers * salt_cost_per_container

    # Calculate the total cost of all food
    total_cost = potato_cost_total + salt_cost_total

    result = total_cost
    return result

print(solution())