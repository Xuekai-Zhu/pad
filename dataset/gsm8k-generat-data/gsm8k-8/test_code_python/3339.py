def solution():
    # Define the increase percentage and the current number of students
    increase_percentage = 20
    current_students = 960

    # Calculate the ratio between the current number of students and 100% + the increase percentage
    ratio = current_students / (100 + increase_percentage)

    # Calculate the number of students last year by multiplying the ratio by 100%
    last_year_students = ratio * 100

    result = last_year_students
    return result

print(solution())