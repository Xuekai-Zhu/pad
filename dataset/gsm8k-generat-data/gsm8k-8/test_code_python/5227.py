def solution():
    # Define the number of legos Julian has and the number required for each airplane model
    julian_legos = 400
    airplane_legos = 240

    # Calculate the total number of legos required for two identical airplane models
    total_airplane_legos = airplane_legos * 2

    # Calculate the remaining legos after making two identical airplane models
    remaining_legos = julian_legos - total_airplane_legos
    result = remaining_legos
    return result

print(solution())