def solution():
    # Calculate the number of students last year
    current_students = 960
    increase_percentage = 20
    previous_students = current_students / (1 + increase_percentage/100)
    result = previous_students
    return result

print(solution())