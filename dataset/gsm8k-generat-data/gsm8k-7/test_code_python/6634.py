def solution():
    boys = 300
    girls_percent = 60
    total_students = boys / (1 - girls_percent/100)
    girls = total_students - boys
    result = girls
    return result

print(solution())