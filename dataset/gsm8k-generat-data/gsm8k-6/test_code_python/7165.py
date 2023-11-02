def solution():
    # Calculate the number of students remaining after the trip to the beach
    students_remaining = 1000 / 2  # Half of the students went on the trip
    students_sent_home = students_remaining / 2  # Half of the remaining students were sent home
    students_in_school = students_remaining - students_sent_home  # Calculate the number of students still in school
    result = students_in_school
    return result

print(solution())