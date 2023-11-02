def solution():
    """The kindergartners each need to bring one mini tissue box to class for the school year. There are three kindergartner groups with 9, 10, and 11 students respectively. Each mini tissue box contains 40 tissues. How many tissues do the kindergartner groups bring together?"""
    num_students_group1 = 9
    num_students_group2 = 10
    num_students_group3 = 11
    num_tissues_per_box = 40
    total_num_students = num_students_group1 + num_students_group2 + num_students_group3
    total_num_boxes = total_num_students // 1  # each student brings one box
    total_num_tissues = total_num_boxes * num_tissues_per_box
    result = total_num_tissues
    return result

print(solution())