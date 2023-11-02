def solution():
    # Calculate the total number of animals on the farm after adding the new ones
    total_cows = 2 + 3  # there are already 2 cows, and 3 more are being added
    total_pigs = 3 + 5  # there are already 3 pigs, and 5 more are being added
    total_goats = 6 + 2  # there are already 6 goats, and 2 more are being added
    total_animals = total_cows + total_pigs + total_goats
    result = total_animals
    return result

print(solution())