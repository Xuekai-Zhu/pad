def solution():
    num_doughnuts_per_box = 10
    total_doughnuts = 300
    num_boxes_sold = 27

    # Calculate the total number of doughnuts sold
    total_doughnuts_sold = num_boxes_sold * num_doughnuts_per_box

    # Calculate the number of doughnuts left over at the end of the day
    doughnuts_left_over = total_doughnuts - total_doughnuts_sold

    result = doughnuts_left_over
    return result

print(solution())