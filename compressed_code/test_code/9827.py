def solution():
    
    boys_percent = 40
    girls_percent = 100 - boys_percent
    boys_grade = 80
    girls_grade = 90
    class_average = (boys_percent/100) * boys_grade + (girls_percent/100) * girls_grade
    result = class_average
    return result

print(solution())