def solution():
    num_students_passed = 200
    growth_rate = 0.5
    current_year = 3

    # Calculate the number of students passed in the current year
    for year in range(current_year):
        num_students_passed = num_students_passed * (1 + growth_rate)

    result = num_students_passed
    return result

print(solution())