def solution():
    pieces_given = 300
    pieces_used = 25 + (2 * 25) + (3 * 25)
    pieces_left = pieces_given - pieces_used
    result = pieces_left
    return result

print(solution())