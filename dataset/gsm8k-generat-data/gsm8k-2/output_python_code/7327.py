def solution():
    """A fifth-grade class went on a field trip to the zoo, and their class of 10 students merged with another class with the same amount of students. 5 parents offered to be a chaperone, and 2 of the teachers from both classes will be there too. When the school day was over, the students could choose to go home and 10 of them left. Two of the chaperones were parents in that group, so they left as well. How many individuals were left at the zoo?"""
    initial_students = 10
    other_class_students = initial_students
    total_students = initial_students + other_class_students
    chaperones = 5
    teachers = 2
    total_people = total_students + chaperones + teachers
    people_left = total_people - 10 - 2
    result = people_left
    return result

print(solution())