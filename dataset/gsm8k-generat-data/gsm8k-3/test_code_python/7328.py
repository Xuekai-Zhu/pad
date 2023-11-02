def solution():
    """A fifth-grade class went on a field trip to the zoo, and their class of 10 students merged with another class with the same amount of students. 5 parents offered to be a chaperone, and 2 of the teachers from both classes will be there too. When the school day was over, the students could choose to go home and 10 of them left. Two of the chaperones were parents in that group, so they left as well. How many individuals were left at the zoo?"""

    # Number of students in each class
    class_size = 10

    # Number of classes on the field trip
    num_classes = 2

    # Number of chaperones
    num_chaperones = 5

    # Number of teachers
    num_teachers = 2

    # Number of students who left after the field trip
    num_students_left = 10

    # Number of chaperones who left after the field trip
    num_chaperones_left = 2

    # Total number of individuals on the field trip
    total_num = (class_size * num_classes) + num_chaperones + num_teachers

    # Number of individuals who left after the field trip
    num_left = num_students_left + num_chaperones_left

    # Number of individuals remaining at the zoo
    num_remaining = total_num - num_left

    # Display the number of individuals remaining
    result = num_remaining
    return result

print(solution())