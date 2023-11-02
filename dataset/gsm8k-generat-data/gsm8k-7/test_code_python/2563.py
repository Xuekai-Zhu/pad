def solution():
    total_cows = 18
    black_cows = int((total_cows/2) + 5)
    non_black_cows = total_cows - black_cows
    result = non_black_cows
    return result

print(solution())