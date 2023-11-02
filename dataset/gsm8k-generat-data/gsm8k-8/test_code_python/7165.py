def solution():
    # Calculate the number of students taken on the trip
    trip_students = 1000 / 2

    # Calculate the number of students remaining after the trip
    remaining_students = 1000 - trip_students

    # Calculate the number of students sent home
    sent_home_students = remaining_students / 2

    # Calculate the number of students still in the school
    students_in_school = remaining_students - sent_home_students
    result = students_in_school
    return result

print(solution())