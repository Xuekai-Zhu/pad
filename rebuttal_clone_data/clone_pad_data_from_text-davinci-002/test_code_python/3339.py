def solution():
    percent_increase = 20
    students_this_year = 960
    increase_amount = students_this_year * (percent_increase / 100)
    total_students = students_this_year + increase_amount
    result = total_students
    return result

print(solution())