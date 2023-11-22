def solution():
    
    # Define the initial number of pomelos
    initial_pomelos = 20

    # Calculate the number of pomelos left after giving away
    pomelos_left = initial_pomelos * (1/4)

    # Calculate the number of pomelos given away
    pomelos_given_away = initial_pomelos - pomelos_left

    # Display the number of pomelos given away
    result = pomelos_given_away
    return result

print(solution())