def solution():
    """Ravi can jump higher than anyone in the class. In fact, he can jump 1.5 times higher than the average jump of the three next highest jumpers. If the three next highest jumpers can jump 23 inches, 27 inches, and 28 inches, how high can Ravi jump?"""
    # Calculate the average jump height of the three next highest jumpers
    avg_jump = (23 + 27 + 28) / 3

    # Calculate Ravi's jump height
    ravi_jump = 1.5 * avg_jump

    # Display Ravi's jump height
    result = ravi_jump
    return result

print(solution())