def solution():
    num_2legged_animals = 10
    num_4legged_animals = 15
    legs_per_2legged = 2
    legs_per_4legged = 4

    # Calculate the total number of legs on all 2-legged animals
    total_legs_2legged = num_2legged_animals * legs_per_2legged

    # Calculate the total number of legs on all 4-legged animals
    total_legs_4legged = num_4legged_animals * legs_per_4legged

    # Calculate the total number of legs on all animals
    total_legs = total_legs_2legged + total_legs_4legged
    result = total_legs
    return result

print(solution())