def solution():
    tissues_per_box = 160  # There are 160 tissues in a tissue box
    num_boxes = 3  # Tucker bought 3 boxes
    tissues_used = 210  # Tucker used 210 tissues while he was sick

    # Calculate the total number of tissues Tucker had before being sick
    total_tissues = tissues_per_box * num_boxes

    # Calculate the number of tissues Tucker has left
    num_tissues_left = total_tissues - tissues_used
    result = num_tissues_left
    return result

print(solution())