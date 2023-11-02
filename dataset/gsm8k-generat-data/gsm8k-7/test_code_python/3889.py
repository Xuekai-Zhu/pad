def solution():
    num_red_pencils = 20
    num_blue_pencils = num_red_pencils * 2
    num_yellow_pencils = 40
    num_green_pencils = num_red_pencils + num_blue_pencils
    pencils_per_box = 20

    # Calculate the total number of pencils
    total_pencils = num_red_pencils + num_blue_pencils + num_yellow_pencils + num_green_pencils

    # Calculate the total number of boxes needed
    total_boxes = total_pencils / pencils_per_box
    result = total_boxes
    return result

print(solution())