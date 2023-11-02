def solution():
    
    total_students = 30
    boys = 10
    girls = 2 * boys
    boy_cups = 5 * boys
    total_cups = 90
    girl_cups = (total_cups - boy_cups) / girls
    result = girl_cups
    return result

print(solution())