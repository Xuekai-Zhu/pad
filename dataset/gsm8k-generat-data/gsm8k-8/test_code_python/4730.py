def solution():
    # Calculate the number of dogs at the farm
    cows_to_dogs_ratio = 2
    number_of_cows = 184
    number_of_dogs = number_of_cows / cows_to_dogs_ratio

    # Determine how many animals will be sold
    number_of_cows_to_sell = number_of_cows / 4
    number_of_dogs_to_sell = number_of_dogs * 3 / 4

    # Calculate the number of animals remaining
    remaining_cows = number_of_cows - number_of_cows_to_sell
    remaining_dogs = number_of_dogs - number_of_dogs_to_sell
    total_remaining_animals = remaining_cows + remaining_dogs

    result = total_remaining_animals
    return result

print(solution())