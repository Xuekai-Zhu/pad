def solution():
    total_students = 60
    students_eating_cafeteria = 10
    students_bringing_lunch = students_eating_cafeteria * 3

    # Calculate the number of students who don't eat lunch
    students_no_lunch = total_students - students_eating_cafeteria - students_bringing_lunch
    result = students_no_lunch
    return result

print(solution())