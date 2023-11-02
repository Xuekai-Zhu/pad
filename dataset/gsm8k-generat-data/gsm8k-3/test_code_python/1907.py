def solution():
    """Ryan builds model mustang cars. A full size mustang is 240 inches long. The mid-size model that Ryan creates is 1/10th the size, and the smallest model that Ryan creates is half the size of the mid-size model. How many inches long is the smallest model mustang?"""
    # Define the length of a full size mustang in inches
    FULL_SIZE_LENGTH = 240

    # Calculate the length of the mid-size model
    MID_SIZE_LENGTH = FULL_SIZE_LENGTH * (1/10)

    # Calculate the length of the smallest model
    SMALLEST_LENGTH = MID_SIZE_LENGTH * (1/2)

    # Display the length of the smallest model in inches
    result = SMALLEST_LENGTH
    return result

print(solution())