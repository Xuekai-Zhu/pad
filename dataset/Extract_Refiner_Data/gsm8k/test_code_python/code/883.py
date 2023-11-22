def solution():
    
    # Define the number of birds nesting in the bushes
    nesting_birds = 6

    # Calculate the number of birds flying overhead
    flying_birds = nesting_birds * (2/3)

    # Calculate the total number of birds
    total_birds = nesting_birds + flying_birds + 3 * 8

    # Display the total number of birds
    result = total_birds
    return result

print(solution())