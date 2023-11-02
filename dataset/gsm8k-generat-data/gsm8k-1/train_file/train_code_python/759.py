def solution():
    """Susan wants to throw a party for her mom. She is planning on having 30 guests. For dinner she is making a recipe that makes 2 servings each. Each batch of the recipe calls for 4 potatoes and 1 teaspoon of salt. A potato costs $.10 and a container of salt costs $2 at the supermarket. If each container of salt has 5 teaspoons, how much money will Susan spend on food?"""
    guests = 30
    servings_per_recipe = 2
    potatoes_per_recipe = 4
    salt_per_recipe = 1
    potatoes_cost = 0.10
    salt_cost_per_container = 2
    salt_per_container = 5
    
    total_servings = guests * servings_per_recipe
    total_recipes = total_servings / servings_per_recipe
    total_potatoes = total_recipes * potatoes_per_recipe
    total_salt = total_recipes * salt_per_recipe
    total_salt_containers = total_salt / salt_per_container
    
    potatoes_cost_total = total_potatoes * potatoes_cost
    salt_cost_total = total_salt_containers * salt_cost_per_container
    
    total_cost = potatoes_cost_total + salt_cost_total
    result = total_cost
    return result

print(solution())