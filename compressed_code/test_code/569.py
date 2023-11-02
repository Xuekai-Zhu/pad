def solution():
    
    lunch_calories = 40
    recommended_calories = 25
    amount_eaten = 0.75 * lunch_calories
    excess_calories = amount_eaten - recommended_calories
    result = excess_calories
    return result

print(solution())