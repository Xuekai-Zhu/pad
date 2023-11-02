def solution():
    # Calculate the number of students in the cafeteria and outside before the commotion
    cafeteria_students = (2/3) * 90
    outside_students = 90 - cafeteria_students

    # Calculate the number of students who jumped from outside to inside
    jumped_students = (1/3) * outside_students

    # Calculate the new number of students in the cafeteria and outside after the commotion
    new_cafeteria_students = cafeteria_students + 3 - jumped_students
    new_outside_students = outside_students - 3 + jumped_students

    result = new_cafeteria_students
    return result

print(solution())