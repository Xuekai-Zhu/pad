def solution():
    total_oil = 290
    num_cans = 24
    partial_cans = 10
    partial_can_size = 8

    # Calculate the total amount of oil in the partial cans
    total_partial_oil = partial_cans * partial_can_size

    # Calculate the total amount of oil in the remaining cans
    remaining_oil = total_oil - total_partial_oil

    # Calculate the size of each remaining can
    remaining_can_size = remaining_oil / (num_cans - partial_cans)

    result = remaining_can_size
    return result

print(solution())