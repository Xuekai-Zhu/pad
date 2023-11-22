def solution():
    
    # Define the initial value of each share
    INITIAL_VALUE = 8 * 8

    # Calculate the new value after the first year
    first_year_increase = INITIAL_VALUE * 0.5
    first_year_new_value = INITIAL_VALUE + first_year_increase

    # Calculate the new value after the second year
    second_year_decrease = INITIAL_VALUE * 0.25
    second_year_new_value = first_year_new_value - second_year_decrease

    # Calculate the final value of all Maria's shares
    final_value = 8 * 8 + second_year_new_value

    # Display the final value
    result = final_value
    return result

print(solution())