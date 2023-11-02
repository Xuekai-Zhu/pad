def solution():
    num_cans = 25
    can_capacity = 8

    # Calculate the total amount of water needed to fill all cans to full capacity
    total_water = num_cans * can_capacity

    # Calculate the amount of water that can be filled in one can at three-quarters capacity
    partial_water = 0.75 * can_capacity

    # Calculate the total number of cans that can be filled with the given truck capacity
    total_partial_cans = 20

    # Calculate the amount of water that can be filled in all partial cans
    total_partial_water = total_partial_cans * partial_water

    # Calculate the time taken to fill all partial cans
    time_partial_cans = 3

    # Calculate the rate of filling for one can at three-quarters capacity
    rate_partial_can = partial_water / time_partial_cans

    # Calculate the time taken to fill all cans to full capacity
    time_full_cans = total_water / rate_partial_can

    result = time_full_cans
    return result

print(solution())