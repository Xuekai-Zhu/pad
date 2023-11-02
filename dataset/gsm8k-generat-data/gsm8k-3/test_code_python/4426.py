def solution():
    """A long wire is cut into three smaller pieces in the ratio of 7:3:2. If the shortest piece is 16 cm, how long was the entire wire before it was cut?"""
    # Define the ratio of the lengths of the three smaller pieces
    ratio = [7, 3, 2]

    # Define the length of the shortest piece
    shortest = 16

    # Calculate the sum of the ratio values
    ratio_sum = sum(ratio)

    # Calculate the length of the entire wire
    total_length = shortest * (ratio_sum / ratio[2])

    # Display the length of the entire wire
    result = total_length
    return result

print(solution())