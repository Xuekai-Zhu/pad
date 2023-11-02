def solution():
    num_boxes_last_week = 10
    num_pomelos_last_week = 240
    num_boxes_this_week = 20

    # Calculate the total number of pomelos shipped
    total_pomelos = num_pomelos_last_week + (num_boxes_this_week * 12)

    # Calculate the total number of dozens of pomelos shipped
    dozens_of_pomelos = total_pomelos / 12

    result = dozens_of_pomelos
    return result

print(solution())