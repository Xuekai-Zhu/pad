def solution():
    num_cows = 184
    num_dogs = num_cows / 2

    # Calculate the number of cows to be sold
    num_cows_to_sell = num_cows / 4

    # Calculate the number of dogs to be sold
    num_dogs_to_sell = num_dogs * 0.75

    # Calculate the number of remaining cows and dogs
    remaining_cows = num_cows - num_cows_to_sell
    remaining_dogs = num_dogs - num_dogs_to_sell

    # Calculate the total number of remaining animals
    total_remaining_animals = remaining_cows + remaining_dogs
    result = total_remaining_animals
    return result

print(solution())