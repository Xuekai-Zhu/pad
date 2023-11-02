def solution():
    
    hens = 3
    eggs_per_day = 3
    days_gone = 7
    eggs_taken = 12
    eggs_laid = hens * eggs_per_day * days_gone
    eggs_remaining = eggs_laid - eggs_taken
    eggs_collected = eggs_remaining - 5
    result = eggs_collected
    return result

print(solution())