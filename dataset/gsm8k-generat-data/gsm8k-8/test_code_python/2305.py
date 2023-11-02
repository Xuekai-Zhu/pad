def solution():
    # Define the ratio of the two parts
    ratio = 2/3

    # Calculate the length of the longer part
    longer_part = 40 * (ratio/(1+ratio))

    # Calculate the length of the shorter part
    shorter_part = 40 - longer_part

    result = shorter_part
    return result

print(solution())