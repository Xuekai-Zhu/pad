def solution():
    
    # Define the initial number of candy pieces
    initial_candy = 100

    # Define the number of candy pieces eaten by Ginger and Amy per day
    ginger_candy_per_day = 4
    amy_candy_per_day = 3

    # Calculate the number of candy pieces eaten by Amy after two weeks
    amy_candy_after_two_weeks = initial_candy - (ginger_candy_per_day * 7 * 2)

    # Calculate the difference in candy pieces between Ginger and Amy
    candy_difference = amy_candy_after_two_weeks - amy_candy_after_two_weeks

    # Display the difference in candy pieces
    result = candy_difference
    return result

print(solution())