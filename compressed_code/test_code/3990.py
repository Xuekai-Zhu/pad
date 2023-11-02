def solution():
    
    initial_cows = 39
    cows_died = 25
    cows_sold = 6
    current_cows = initial_cows - cows_died - cows_sold
    current_cows += 24
    current_cows += 43
    current_cows += 8
    result = current_cows
    return result

print(solution())