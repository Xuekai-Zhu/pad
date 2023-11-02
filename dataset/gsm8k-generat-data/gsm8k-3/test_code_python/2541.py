def solution():
    """The bald eagle can dive at a speed of 100 miles per hour, while the peregrine falcon can dive at a speed of twice that of the bald eagle. Starting from the same treetop, if it takes the bald eagle 30 seconds to dive to the ground, how long, in seconds, will it take the peregrine falcon to dive the same distance?"""
    # Define the speed of the bald eagle and the peregrine falcon
    BALD_EAGLE_SPEED = 100
    PEREGRINE_FALCON_SPEED = 2 * BALD_EAGLE_SPEED

    # Define the time it takes the bald eagle to dive to the ground
    BALD_EAGLE_TIME = 30

    # Calculate the time it takes the peregrine falcon to dive the same distance
    PEREGRINE_FALCON_TIME = BALD_EAGLE_TIME * BALD_EAGLE_SPEED / PEREGRINE_FALCON_SPEED

    # Display the time it takes the peregrine falcon to dive the same distance
    result = PEREGRINE_FALCON_TIME
    return result

print(solution())