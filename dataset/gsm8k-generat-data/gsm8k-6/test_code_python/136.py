def solution():
    # Calculate the number of small animals Loraine made
    num_small_animals = 12 / 2  # each small animal takes 2 sticks of wax

    # Calculate the number of large animals Loraine made
    num_large_animals = num_small_animals / 3  # three times as many small animals as large animals, so divide by 3

    # Calculate the total sticks of wax Loraine used
    total_wax_sticks = 4 * num_large_animals + 2 * num_small_animals

    result = total_wax_sticks
    return result

print(solution())