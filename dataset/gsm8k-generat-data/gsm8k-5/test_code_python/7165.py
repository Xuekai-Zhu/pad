def solution():
    # Find the number of students taken on a trip
    students_on_trip = 1000/2

    # Find the number of remaining students
    remaining_students = 1000 - students_on_trip

    # Find the number of students sent home
    sent_home = remaining_students/2

    # Find the number of students remaining in school
    remaining_in_school = remaining_students - sent_home
    result = remaining_in_school
    return result

print(solution())