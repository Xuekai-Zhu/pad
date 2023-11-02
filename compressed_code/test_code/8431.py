def solution():
    
    current_students = 960
    percent_increase = 20
    previous_students = current_students / (1 + (percent_increase / 100))
    result = previous_students
    return result

print(solution())