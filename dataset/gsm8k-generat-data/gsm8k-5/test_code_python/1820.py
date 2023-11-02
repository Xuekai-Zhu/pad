def solution():
    chocolates_in_boxes = 3 * 3  # 3 boxes, each with 3 chocolates
    chocolates_not_in_box = 5  # 5 chocolates not in a box
    total_chocolates = chocolates_in_boxes + chocolates_not_in_box  # Total number of chocolates

    # Calculate the number of chocolates needed to fill a box
    chocolates_per_box = 25 / 3  # Each box needs to have 25/3 chocolates

    # Calculate the number of boxes needed to store all the chocolates
    total_boxes_needed = (total_chocolates + 25) / chocolates_per_box  # Add the chocolates brought by friend

    # Calculate the number of additional boxes needed
    additional_boxes_needed = total_boxes_needed - 3  # Subtract the 3 boxes already filled

    result = additional_boxes_needed
    return result

print(solution())