def solution():
    num_long_wood = 6
    long_wood_length = 4
    num_short_wood = 2
    short_wood_length = 2

    # Calculate the total length of all long wood
    total_long_wood_length = num_long_wood * long_wood_length

    # Calculate the total length of all short wood
    total_short_wood_length = num_short_wood * short_wood_length

    # Calculate the total length of all wood needed
    total_wood_length = total_long_wood_length + total_short_wood_length
    result = total_wood_length
    return result

print(solution())