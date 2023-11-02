def solution():
    total_students = 60
    cafeteria_students = 10
    lunch_bringer_students = cafeteria_students * 3

    # Calculate the total number of students who eat lunch
    total_lunch_students = cafeteria_students + lunch_bringer_students

    # Calculate the number of students who don't eat lunch
    no_lunch_students = total_students - total_lunch_students
    result = no_lunch_students
    return result

print(solution())