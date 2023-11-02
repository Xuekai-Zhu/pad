def solution():
    brown_eyes = 6
    brown_eyes_percentage = 2/3
    black_hair_percentage = 1/2

    # Calculate total number of students with brown eyes
    total_brown_eyes = brown_eyes / black_hair_percentage

    # Calculate total number of students in the class
    total_students = total_brown_eyes / brown_eyes_percentage

    result = total_students
    return result

print(solution())