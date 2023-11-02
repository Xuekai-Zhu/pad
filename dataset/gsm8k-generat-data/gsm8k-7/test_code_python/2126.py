def solution():
    initial_students = 40
    annual_increase = 10
    num_years = 10

    # Calculate the total number of students Adam will teach over 10 years
    total_students = ((num_years-1) * annual_increase) + initial_students + 50

    result = total_students
    return result

print(solution())