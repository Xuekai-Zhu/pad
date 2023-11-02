def solution():
    # Calculate the total amount of water that can be filled in 20 cans
    total_water = 20 * (8 * 0.75)  # each can is filled with 3/4 of its capacity

    # Calculate the amount of water that can be filled in one can when it is filled to full capacity
    one_can_water = 8 * 1  # each can is filled with 1 gallon of water

    # Calculate how long it will take to fill 25 cans
    time_to_fill_25_cans = (total_water + (25 * one_can_water)) / (20 * one_can_water * 3)

    result = time_to_fill_25_cans
    return result

print(solution())