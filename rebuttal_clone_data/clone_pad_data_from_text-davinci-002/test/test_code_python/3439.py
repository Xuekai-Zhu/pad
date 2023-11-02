def solution():
    original_cows = 51
    new_cows = 5
    total_cows = original_cows + new_cows
    quarter_cows = total_cows / 4
    remaining_cows = total_cows - quarter_cows
    result = remaining_cows
    return result

print(solution())