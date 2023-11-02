def solution():
    total_eggs_in_pounds = 6
    weight_of_one_egg_in_pounds = 1/16
    num_eggs = total_eggs_in_pounds / weight_of_one_egg_in_pounds

    # Calculate the number of dozens of eggs
    num_dozens = num_eggs / 12
    result = num_dozens
    return result

print(solution())