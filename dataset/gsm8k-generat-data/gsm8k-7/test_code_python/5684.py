def solution():
    num_groups = 3  # number of kindergartner groups
    num_students = [9, 10, 11]  # number of students in each group
    tissues_per_box = 40  # number of tissues per mini tissue box

    # Calculate the total number of mini tissue boxes needed
    total_boxes = sum(num_students)

    # Calculate the total number of tissues needed
    total_tissues = total_boxes * tissues_per_box
    result = total_tissues
    return result

print(solution())