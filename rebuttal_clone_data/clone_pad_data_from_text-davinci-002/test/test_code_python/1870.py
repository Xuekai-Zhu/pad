def solution():
    space_available = 10 * 15
    vegetables_planted = 5 + 5 + 5 + 4 + 4 + 4 + 4 + 4 + 30
    space_used = vegetables_planted
    space_left = space_available - space_used
    result = space_left
    return result

print(solution())