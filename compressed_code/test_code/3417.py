def solution():
    
    quarters_before = 160
    cost = 35
    quarters_per_dollar = 4    
    quarters_spent = cost * quarters_per_dollar
    quarters_after = quarters_before - quarters_spent
    result = quarters_after
    return result

print(solution())