def solution():
    # Define the initial amount of water in the tank
    initial_water = 100 * 2 / 5

    # Calculate the amount of water collected on the first and second days
    first_day = 15
    second_day = first_day + 5

    # Calculate the amount of water remaining after the first and second days
    remaining_water = 100 - initial_water - first_day - second_day

    # Calculate the amount of water collected on the third day
    third_day = remaining_water

    result = third_day
    return result

print(solution())