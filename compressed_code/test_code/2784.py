def solution():
    
    total_students = 140
    dancer_students = total_students / 4
    slow_dance_students = 25
    non_slow_dance_students = dancer_students - slow_dance_students
    result = non_slow_dance_students
    return result

print(solution())