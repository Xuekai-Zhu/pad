def solution():
    num_students_yesterday = 70
    num_students_absent_today = 30
    
    # Calculate the total number of students present today
    num_students_today = (2*num_students_yesterday - 10*num_students_yesterday/100) - num_students_absent_today
    
    # Calculate the total number of registered students for the course
    total_registered_students = num_students_today + num_students_absent_today
    result = total_registered_students
    return result

print(solution())