def solution():
    """Xena is trying to outrun a dragon to get to the safety of a cave it's too big to fit into. Xena has a 600 foot head start, but the dragon can burn her if it gets within 120 feet of her. If Xena runs 15 feet per second and the dragon flies 30 feet per second, how many seconds does Xena have to get to the cave?"""
    # Define Xena's initial position and speed
    xena_position = 600
    xena_speed = 15

    # Define the dragon's initial position and speed
    dragon_position = 0
    dragon_speed = 30

    # Define the distance at which the dragon can burn Xena
    burn_distance = 120

    # Initialize the time counter
    time = 0

    # Calculate the time it takes for Xena to reach the cave
    while xena_position - dragon_position > burn_distance:
        time += 1
        xena_position += xena_speed
        dragon_position += dragon_speed
    
    # Return the time Xena has to get to the cave
    result = time
    return result

print(solution())