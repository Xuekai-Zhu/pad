def solution():
    """Ravi can jump higher than anyone in the class. In fact, he can jump 1.5 times higher than the average jump of the three next highest jumpers. If the three next highest jumpers can jump 23 inches, 27 inches, and 28 inches, how high can Ravi jump?"""
    # Define the heights of the three next highest jumpers
    jumper_heights = [23, 27, 28]

    # Calculate the average jump height of the three next highest jumpers
    avg_jumper_height = sum(jumper_heights) / len(jumper_heights)

    # Calculate Ravi's jump height
    ravi_jump_height = avg_jumper_height * 1.5

    # return the result
    result = ravi_jump_height
    return result

print(solution())