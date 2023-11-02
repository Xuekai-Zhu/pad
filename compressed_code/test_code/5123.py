def solution():
    
    boys = 300
    girl_percentage = 60
    total_students = boys / (100 - girl_percentage) * 100
    girls = total_students - boys
    result = girls
    return result

print(solution())