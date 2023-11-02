def solution():
    num_guests = 30
    recipe_servings = 2
    num_batches = num_guests / recipe_servings
    potatoes_per_batch = 4
    teaspoons_per_container = 5
    containers_of_salt = 1 / teaspoons_per_container
    cost_per_potato = .10
    cost_per_container = 2
    total_cost = (num_batches * potatoes_per_batch * cost_per_potato) + (num_batches * containers_of_salt * cost_per_container)
    result = total_cost
    return result

print(solution())