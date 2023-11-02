def solution():
    
    # Define the initial number of pomelos
    initial_pomelos = 20

    # Calculate the number of pomelos Eve has left
    left_pomelos = initial_pomelos * (1/4)

    # Calculate the number of pomelos Eve gave away
    given_pomelos = initial_pomelos - left_pomelos

    # Display the number of pomelos Eve gave away
    result = given_pomelos
    return result

print(solution())