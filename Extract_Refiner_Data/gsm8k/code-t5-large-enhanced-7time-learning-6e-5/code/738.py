def solution():
    
    total_students = 80
    girls_percent = 40
    girls_per_class = (girls_percent / 100) * total_students
    boys_per_class = total_students - girls_per_class
    result = boys_per_class
    return result

print(solution())