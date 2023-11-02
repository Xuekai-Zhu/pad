def solution():
    total_students = 100
    girl_students = total_students / 2
    boy_students = total_students / 2
    girl_students_with_dogs = girl_students * 0.2
    boy_students_with_dogs = boy_students * 0.1
    total_students_with_dogs = girl_students_with_dogs + boy_students_with_dogs
    result = total_students_with_dogs
    return result

print(solution())