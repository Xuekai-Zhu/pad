def solution():
    # Define the total number of brownies
    total_brownies = 24

    # Calculate the number of brownies Tina ate
    tina_brownies = 2 * 5

    # Calculate the number of brownies Tina's husband took to work
    husband_brownies = 1 * 5

    # Calculate the number of brownies shared with guests
    guest_brownies = 4

    # Subtract the eaten and shared brownies from the total to find the remaining brownies
    remaining_brownies = total_brownies - tina_brownies - husband_brownies - guest_brownies

    result = remaining_brownies
    return result

print(solution())