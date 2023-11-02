def solution():
     current_cups = 15
     increase_percentage = 40
     recommended_cups = current_cups + (current_cups * (increase_percentage/100))
     result = recommended_cups
     return result

print(solution())