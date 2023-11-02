def solution():
    
    total_students = 1000
    beach_students = total_students / 2
    remaining_students = total_students - beach_students
    sent_home_students = remaining_students / 2
    remaining_students = remaining_students - sent_home_students
    result = remaining_students
    return result

print(solution())