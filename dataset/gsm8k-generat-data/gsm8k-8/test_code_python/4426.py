def solution():
    # Define the ratio of the three pieces
    ratio = [7, 3, 2]

    # Calculate the total ratio
    total_ratio = sum(ratio)

    # Calculate the length of the shortest piece
    shortest_length = 16

    # Calculate the length of the entire wire
    total_length = shortest_length * total_ratio / ratio[-1]
    result = total_length
    return result

print(solution())