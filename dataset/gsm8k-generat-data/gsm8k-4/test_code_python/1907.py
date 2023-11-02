def solution():
    """Ryan builds model mustang cars. A full size mustang is 240 inches long. The mid-size model that Ryan creates is 1/10th the size, and the smallest model that Ryan creates is half the size of the mid-size model. How many inches long is the smallest model mustang?"""
    # Define the length of a full size mustang
    full_size_length = 240

    # Calculate the length of the mid-size model
    mid_size_length = full_size_length / 10

    # Calculate the length of the smallest model
    smallest_length = mid_size_length / 2

    # Return the length of the smallest model
    result = smallest_length
    return result

print(solution())