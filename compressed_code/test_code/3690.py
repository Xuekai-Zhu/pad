def solution():
    
    current_cups = 15
    increase_percentage = 0.4
    recommended_cups = current_cups + (current_cups * increase_percentage)
    result = recommended_cups
    return result

print(solution())