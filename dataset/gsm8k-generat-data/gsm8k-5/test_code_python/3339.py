def solution():
    # Calculate the percentage increase
    percentage_increase = 20 / 100

    # Calculate the number of students last year by dividing the current number by 1 + the percentage increase
    last_year_students = round(960 / (1 + percentage_increase))

    result = last_year_students
    return result

print(solution())