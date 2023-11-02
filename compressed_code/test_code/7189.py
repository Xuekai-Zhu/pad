def solution():
    
    total_students = 30
    girls = 18
    green = total_students / 2
    pink = girls / 3
    yellow = total_students - (green + pink)
    result = yellow
    return result

print(solution())