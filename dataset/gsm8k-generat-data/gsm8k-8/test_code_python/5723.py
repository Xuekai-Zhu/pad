def solution():
    # Define the number of tissues in each box and the number of boxes Tucker bought
    num_tissues_per_box = 160
    num_boxes_bought = 3

    # Calculate the total number of tissues Tucker had before getting sick
    total_tissues_before_sickness = num_boxes_bought * num_tissues_per_box

    # Calculate the number of tissues Tucker has left after being sick
    num_tissues_left = total_tissues_before_sickness - 210
    result = num_tissues_left
    return result

print(solution())