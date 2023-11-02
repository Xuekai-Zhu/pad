def solution():
    
    # Define the volume of sauce and the number of tomatoes per can
    sauce_volume = 32
    tomatoes_per_can = 3

    # Calculate the total volume of sauce used
    total_sauce_volume = sauce_volume / tomatoes_per_can

    # Calculate the number of tomatoes used
    tomatoes_used = total_sauce_volume / tomatoes_per_can

    # Display the number of tomatoes used
    result = tomatoes_used
    return result

print(solution())