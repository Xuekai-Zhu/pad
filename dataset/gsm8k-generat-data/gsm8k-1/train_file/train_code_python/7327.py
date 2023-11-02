def solution():
    """A fifth-grade class went on a field trip to the zoo, and their class of 10 students merged with another class with the same amount of students. 5 parents offered to be a chaperone, and 2 of the teachers from both classes will be there too. When the school day was over, the students could choose to go home and 10 of them left. Two of the chaperones were parents in that group, so they left as well. How many individuals were left at the zoo?"""
    class_size = 10
    merged_class_size = 10
    num_chaperones = 5
    num_teachers = 2
    num_students_left = 10
    num_parent_chaperones_left = 2
    total_num_people = (class_size + merged_class_size + num_chaperones + num_teachers) - (
            num_students_left + num_parent_chaperones_left)
    result = total_num_people
    return result

print(solution())