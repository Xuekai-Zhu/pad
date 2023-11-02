def solution():
    # Calculate the number of NYC residents who visit the museum
    nyc_residents = 200 / 2

    # Calculate the number of NYC residents who are college students
    college_students = nyc_residents * 0.3

    # Calculate the revenue from college students who are NYC residents
    revenue = college_students * 4

    result = revenue
    return result

print(solution())