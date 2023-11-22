def solution():
    
    # Define the number of homes built in the first year
    homes_1 = 12

    # Define the number of homes built in the second year
    homes_2 = 3 * homes_1

    # Define the number of homes built in the third year
    homes_3 = homes_2 * 2

    # Calculate the total number of homes built over the next three years
    total_homes = homes_1 + homes_2 + homes_3

    # Display the total number of homes built
    result = total_homes
    return result

print(solution())