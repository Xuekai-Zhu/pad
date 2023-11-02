def solution():
    
    total_toys = 9
    total_worth = 52
    one_toy_worth = 12
    other_toy_worth = (total_worth - one_toy_worth) / (total_toys - 1)
    result = other_toy_worth
    return result

print(solution())