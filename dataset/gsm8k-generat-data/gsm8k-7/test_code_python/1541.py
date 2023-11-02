def solution():
    num_bunches = 8
    flowers_per_bunch_1 = 9
    flowers_per_bunch_2 = 12

    # Calculate the total number of flowers in the original bunches
    total_flowers_1 = num_bunches * flowers_per_bunch_1

    # Calculate the total number of bunches needed for 12 flowers per bunch
    num_bunches_2 = total_flowers_1 // flowers_per_bunch_2

    # If there are any remaining flowers, add another bunch
    if total_flowers_1 % flowers_per_bunch_2 != 0:
        num_bunches_2 += 1

    result = num_bunches_2
    return result

print(solution())