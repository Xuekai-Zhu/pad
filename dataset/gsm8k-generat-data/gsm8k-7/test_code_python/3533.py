def solution():
    # Calculate the side lengths of squares A and B
    side_length_A = math.sqrt(25)
    side_length_B = math.sqrt(81)

    # Calculate the difference between the side lengths
    side_length_diff = abs(side_length_A - side_length_B)

    result = side_length_diff
    return result

print(solution())