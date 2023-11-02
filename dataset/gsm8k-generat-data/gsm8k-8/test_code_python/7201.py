def solution():
    # Calculate the number of visitors that are residents of NYC
    nyc_residents = 200 / 2

    # Calculate the number of NYC residents that are college students
    college_students = 0.3 * nyc_residents

    # Calculate the revenue from college student tickets
    revenue = college_students * 4
    result = revenue
    return result

print(solution())