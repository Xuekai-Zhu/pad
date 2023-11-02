def solution():
    
    initial_cows = 200
    years = 2
    total_cows = initial_cows * ((1 + 0.5) ** years)
    result = total_cows
    return result

print(solution())