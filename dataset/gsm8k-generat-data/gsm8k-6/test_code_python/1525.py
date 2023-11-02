def solution():
    # Find the total number of students in the Biology class
    physics_class = 200
    biology_class = physics_class / 2
    total_students = physics_class + biology_class 

    # Calculate the number of girls and boys in the Biology class
    girls = 3/4 * total_students
    boys = 1/4 * total_students
    result = boys
    return result

print(solution())