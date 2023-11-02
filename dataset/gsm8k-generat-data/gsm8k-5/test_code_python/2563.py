def solution():
    total_cows = 18  # Sam has 18 cows
    black_cows = (total_cows // 2) + 5  # 5 more than half the cows are black
    non_black_cows = total_cows - black_cows  # Calculate the number of non-black cows
    result = non_black_cows
    return result

print(solution())