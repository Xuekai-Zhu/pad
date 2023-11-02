def solution():
    total_cows = 18 
    black_cows = (total_cows / 2) + 5  # 5 more than half of all cows are black
    non_black_cows = total_cows - black_cows  # subtract the number of black cows from the total to get the number of non-black cows
    result = non_black_cows
    return result

print(solution())