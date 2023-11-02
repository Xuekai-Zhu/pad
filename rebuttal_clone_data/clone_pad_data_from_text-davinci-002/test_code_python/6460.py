def solution():
    white_stones = 40
    black_stones = 60
    total_stones = 100
    result = ((total_stones - white_stones - black_stones) / 2) + white_stones
    return result

print(solution())