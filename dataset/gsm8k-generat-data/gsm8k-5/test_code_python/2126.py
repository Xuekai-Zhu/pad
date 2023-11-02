def solution():
    students_first_year = 40  # Adam teaches 40 students in the first year
    total_years = 10  # Adam will teach for 10 years
    total_students = students_first_year  # Start with the number of students in the first year

    # Calculate the total number of students Adam will teach in 10 years
    for year in range(2, total_years + 1):
        total_students += 50  # Adam teaches 50 students each year after the first year

    result = total_students
    return result

print(solution())