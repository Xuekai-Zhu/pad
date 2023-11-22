def solution():
    
    # Define the number of blocks and stuffed animals
    blocks = 31
    stuffed_animals = 8

    # Define the number of multicolored rings
    multicolored_rings = 9

    # Calculate the total number of toys
    total_toys = blocks + stuffed_animals + multicolored_rings

    # Calculate the number of bouncy balls in the tube
    bouncy_balls = 62 - total_toys

    # Display the number of bouncy balls
    result = bouncy_balls
    return result

print(solution())