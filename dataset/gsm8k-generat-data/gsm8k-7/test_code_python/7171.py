def solution():
    colors_of_crayons = 4
    crayons_per_color_in_box = 2
    boxes_per_hour = 5
    hours = 4

    # Calculate the total number of boxes produced in 4 hours
    total_boxes = boxes_per_hour * hours

    # Calculate the total number of crayons in one box
    total_crayons_in_box = colors_of_crayons * crayons_per_color_in_box

    # Calculate the total number of crayons produced in 4 hours
    total_crayons = total_boxes * total_crayons_in_box
    result = total_crayons
    return result

print(solution())