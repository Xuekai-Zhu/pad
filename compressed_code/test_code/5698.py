def solution():
    
    num_girls_reading = 5/6 * 12
    num_boys_reading = 4/5 * 10
    num_students_reading = num_girls_reading + num_boys_reading
    total_students = 12 + 10
    num_students_not_reading = total_students - num_students_reading
    result = num_students_not_reading
    return result

print(solution())