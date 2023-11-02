def solution():
    num_students = 10
    num_classes = 2
    num_chaperones = 5
    num_teachers = 2
    num_students_left = 10
    num_chaperones_left = 2

    # Calculate the total number of students
    total_students = num_students * num_classes

    # Calculate the total number of people at the zoo before some left
    total_people = total_students + num_chaperones + num_teachers

    # Calculate the number of people who left the zoo
    num_people_left = num_students_left + num_chaperones_left

    # Calculate the number of people who are still at the zoo
    num_people_remaining = total_people - num_people_left
    result = num_people_remaining
    return result

print(solution())