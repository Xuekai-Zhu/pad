def solution():
    """The last time Bob cut his hair he cut it to 6 inches.  His hair is now 36 inches long. If hair grows at a rate of .5 inches per month how many years did it take him to grow out his hair?"""
    # Define the initial length of Bob's hair and the rate of hair growth
    initial_length = 6
    growth_rate = 0.5

    # Define the final length of Bob's hair
    final_length = 36

    # Calculate the difference in length and divide by the growth rate to get the time
    growth_length = final_length - initial_length
    time_in_months = growth_length / growth_rate
    time_in_years = time_in_months / 12

    # Display the time it took for Bob to grow out his hair
    result = time_in_years
    return result

print(solution())