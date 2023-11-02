def solution():
    shortest_piece = 16  # The shortest piece is 16 cm
    ratio = 7 + 3 + 2  # The ratio of the lengths of the three pieces is 7:3:2

    # Calculate the length of the shortest piece in terms of the ratio
    shortest_length = shortest_piece / (2 + 3 + 7)

    # Calculate the length of the longer pieces in terms of the ratio
    middle_length = shortest_length * 3
    longest_length = shortest_length * 7

    # Calculate the total length of the wire
    total_length = shortest_piece / shortest_length * ratio
    result = total_length
    return result

print(solution())