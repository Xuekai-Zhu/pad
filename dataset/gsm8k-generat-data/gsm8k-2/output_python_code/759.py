def solution():
    """Susan wants to throw a party for her mom. She is planning on having 30 guests. For dinner she is making a recipe that makes 2 servings each. Each batch of the recipe calls for 4 potatoes and 1 teaspoon of salt. A potato costs $.10 and a container of salt costs $2 at the supermarket. If each container of salt has 5 teaspoons, how much money will Susan spend on food?"""
    num_guests = 30
    num_servings = num_guests / 2
    num_batches = num_servings / 2
    num_potatoes = num_batches * 4
    num_salt_teaspoons = num_batches * 1
    num_salt_containers = (num_salt_teaspoons / 5) + 1
    potato_cost = num_potatoes * 0.1
    salt_cost = num_salt_containers * 2
    total_cost = potato_cost + salt_cost
    result = total_cost
    return result

print(solution())