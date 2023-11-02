def solution():
    """Jake and Penny are hunting snakes. Jake's snake is 12 inches longer than Jenny's snake. If the two snakes have a combined length of 70 inches, how long is Jake's snake?"""
    total_length = 70
    jenny_length = (total_length - 12) / 2
    jake_length = jenny_length + 12
    result = jake_length
    return result

print(solution())