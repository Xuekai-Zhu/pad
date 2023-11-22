def solution():
    
    # Define the number of rolls made
    rolls_made = 12

    # Define the number of children
    children = 6

    # Calculate the number of rolls left
    rolls_left = rolls_made - children

    # Calculate the number of rolls that were broken into 8 pieces
    rolls_broken = rolls_left * 8

    # Calculate the number of rolls fed to the chickens
    rolls_fed = rolls_broken

    # Display the number of rolls fed to the chickens
    result = rolls_fed
    return result

print(solution())