def solution():
    
    # Define the initial number of sandwiches
    sandwiches = 12

    # Calculate the number of sandwiches Cody ate
    cody_sandwiches = sandwiches // 3

    # Calculate the number of sandwiches Trevor ate
    trevor_sandwiches = sandwiches // 4

    # Calculate the number of sandwiches left
    sandwiches_left = sandwiches - cody_sandwiches - trevor_sandwiches

    # Display the number of sandwiches left
    result = sandwiches_left
    return result

print(solution())