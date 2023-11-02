def solution():
    
    initial_cows = 51
    new_cows = 5
    total_cows = initial_cows + new_cows
    cows_sold = total_cows // 4
    remaining_cows = total_cows - cows_sold
    result = remaining_cows
    return result

print(solution())