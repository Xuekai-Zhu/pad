def solution():
    """A long wire is cut into three smaller pieces in the ratio of 7:3:2. If the shortest piece is 16 cm, how long was the entire wire before it was cut?"""
    shortest_piece = 16
    ratio_sum = 7 + 3 + 2
    total_length = shortest_piece / (2/ ratio_sum)
    result = total_length
    return result

print(solution())