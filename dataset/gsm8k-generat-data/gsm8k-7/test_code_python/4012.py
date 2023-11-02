def solution():
    num_cats = 2
    num_dogs = 3
    cost_per_night = 13

    # Calculate the total number of animals
    total_animals = num_cats + num_dogs

    # Calculate the total cost for one night
    total_cost_per_night = total_animals * cost_per_night

    result = total_cost_per_night
    return result

print(solution())