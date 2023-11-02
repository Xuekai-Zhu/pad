def solution():
    
    current_cups = 15
    increase_percent = 40
    increase_amount = current_cups * (increase_percent / 100)
    recommended_cups = current_cups + increase_amount
    result = recommended_cups
    return result

print(solution())