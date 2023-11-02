def solution():
    """Ryan builds model mustang cars. A full size mustang is 240 inches long. The mid-size model that Ryan creates is 1/10th the size, and the smallest model that Ryan creates is half the size of the mid-size model. How many inches long is the smallest model mustang?"""
    full_size = 240
    mid_size = full_size * (1/10)
    small_size = mid_size * (1/2)
    result = small_size
    return result

print(solution())