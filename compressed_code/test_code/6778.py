def solution():
    
    total_toothpaste = 105
    grams_per_day = (3+2+1+1) * 3
    days_until_empty = total_toothpaste // grams_per_day
    result = days_until_empty
    return result

print(solution())