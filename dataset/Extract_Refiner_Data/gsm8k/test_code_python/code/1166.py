def solution():
    
    # Define the total number of pints of paint used
    total_pints = 12

    # Calculate the number of yellow paint in the mural
    yellow_pints = total_pints / 2

    # Calculate the number of red, white, and purple paint in the mural
    red_pints = total_pints - yellow_pints

    # Display the number of pints of red paint used
    result = red_pints
    return result

print(solution())