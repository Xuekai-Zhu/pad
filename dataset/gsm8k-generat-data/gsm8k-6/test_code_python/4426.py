def solution():
    # Calculate the total length of the wire before it was cut
    shortest_piece = 2  # Given that the shortest piece is 16 cm and its ratio is 2 in 7:3:2
    total_ratio = 7 + 3 + 2  # as per the given ratio
    total_length = (shortest_piece / 2) * total_ratio  # dividing by the ratio to get the length of each part
    result = total_length
    return result

print(solution())