def solution():
    # Define the ratio of long side to short side
    ratio = 3

    # Define the total length of the fence
    total_length = 640

    # Calculate the perimeter of the rectangular plot
    perimeter = total_length / 2

    # Calculate the length of each side
    short_side = perimeter / (ratio + 1)
    long_side = ratio * short_side

    # Calculate the length of the rusted side
    rusted_side = short_side

    result = rusted_side
    return result

print(solution())