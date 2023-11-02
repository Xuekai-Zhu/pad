def solution():
    
    cups_per_dog_per_day = 1.5 * 3
    total_cups_per_day = cups_per_dog_per_day * 2
    cups_per_pound = 2.25
    total_pounds_per_day = total_cups_per_day / cups_per_pound
    result = total_pounds_per_day
    return result

print(solution())