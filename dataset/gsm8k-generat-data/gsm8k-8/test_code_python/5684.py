def solution():
    # Define the number of students in each group
    group1_students = 9
    group2_students = 10
    group3_students = 11

    # Define the number of tissues in each mini box
    tissues_per_box = 40

    # Calculate the total number of boxes needed
    total_boxes = group1_students + group2_students + group3_students

    # Calculate the total number of tissues needed
    total_tissues = total_boxes * tissues_per_box
    result = total_tissues
    return result

print(solution())