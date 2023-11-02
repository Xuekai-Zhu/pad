def solution():
    
    first_protest_days = 4
    second_protest_percentage_increase = 25
    second_protest_days = first_protest_days * (1 + (second_protest_percentage_increase / 100))
    total_days = first_protest_days + second_protest_days
    result = total_days
    return result

print(solution())