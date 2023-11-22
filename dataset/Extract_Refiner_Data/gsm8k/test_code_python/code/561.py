def solution():
    
    # Define the initial number of sandwiches
    initial_sandwiches = 12

    # Calculate the number of sandwiches Cody ate
    cody_sandwiches = initial_sandwiches // 3

    # Calculate the number of sandwiches Trevor ate
    trevor_sandwiches = initial_sandwiches // 4

    # Calculate the total number of sandwiches eaten
    total_sandwiches_eaten = cody_sandwiches + trevor_sandwiches

    # Calculate the number of sandwiches left
    sandwiches_left = initial_sandwiches - total_sandwiches_eaten

    # Display the number of sandwiches left
    result = sandwiches_left
    return result

print(solution())