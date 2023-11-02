def solution():
    # Initialize variables
    num_students = 200
    year = 3

    # Calculate number of students for each subsequent year
    while year <= 2021-2018: # assume current year is 2021
        num_students *= 1.5
        year += 1

    result = round(num_students)
    return result

print(solution())