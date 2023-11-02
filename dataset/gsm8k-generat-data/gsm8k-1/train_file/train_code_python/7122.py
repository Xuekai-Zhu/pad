def solution():
    """Harrison Elementary School is overcrowded with 1590 students, so 40% of the students are going to move to a new school. There are 3 grade levels, and each grade level needs one 20-person advanced class and the rest of the students divided evenly into 6 additional classes. How many students will there be in each normal class at the new school?"""
    total_students = 1590
    move_percent = 0.4
    remaining_students = total_students * (1 - move_percent)
    num_grade_levels = 3
    advanced_class_size = 20
    num_regular_classes = 6
    regular_class_size = int((remaining_students / num_grade_levels - advanced_class_size) / num_regular_classes)
    result = regular_class_size
    return result

print(solution())