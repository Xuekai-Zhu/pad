def solution():
    """The kindergartners each need to bring one mini tissue box to class for the school year. There are three kindergartner groups with 9, 10, and 11 students respectively. Each mini tissue box contains 40 tissues. How many tissues do the kindergartner groups bring together?"""
    group1_students = 9
    group2_students = 10 
    group3_students = 11
    minibox_tissues = 40
    total_boxes = group1_students + group2_students + group3_students
    total_tissues = total_boxes * minibox_tissues 
    result = total_tissues
    return result

print(solution())