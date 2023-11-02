def solution():
    
    # Define the number of homes built in the first year
    homes_first_year = 12

    # Define the number of homes built in the next year
    homes_next_year = homes_first_year * 3

    # Define the number of homes built in the third year
    homes_third_year = homes_next_year * 2

    # Calculate the total number of homes built over the next three years
    total_homes = homes_first_year + homes_next_year + homes_third_year

    # Display the total number of homes built
    result = total_homes
    return result

print(solution())