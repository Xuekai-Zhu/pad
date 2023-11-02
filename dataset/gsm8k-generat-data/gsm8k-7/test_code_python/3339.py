def solution():
    current_year_students = 960
    percent_increase = 0.20
    # Calculate the number of students last year by subtracting the 20% increase from the current year's total.
    last_year_students = current_year_students / (1 + percent_increase) * (1 - percent_increase)
    result = last_year_students
    return result

print(solution())