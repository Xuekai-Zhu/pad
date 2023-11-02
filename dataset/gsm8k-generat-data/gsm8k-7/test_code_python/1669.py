def solution():
    total_animals = 200
    num_cows = 40
    num_sheep = 56

    # Calculate the number of goats in the field
    num_goats = total_animals - num_cows - num_sheep
    result = num_goats
    return result

print(solution())