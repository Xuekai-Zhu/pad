def solution():
    # Calculate the difference in weight between Jack and Anna
    weight_difference = abs(60 - 40)

    # Calculate the number of 4-pound rocks needed
    rocks_needed = weight_difference / 4

    # Round up to the nearest whole number
    rocks_needed = math.ceil(rocks_needed)

    result = rocks_needed
    return result

print(solution())