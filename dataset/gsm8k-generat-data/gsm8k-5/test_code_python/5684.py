def solution():
    num_groups = 3
    group_sizes = [9, 10, 11]
    num_tissues_per_box = 40

    # Calculate the total number of mini tissue boxes needed
    total_boxes = sum(group_sizes)

    # Calculate the total number of tissues needed
    total_tissues = total_boxes * num_tissues_per_box
    result = total_tissues
    return result

print(solution())