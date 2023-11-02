def solution():
    chocolates_in_boxes = 3 * 50 # chocolates in filled boxes
    chocolates_not_in_box = 5 # chocolates not in a box
    friend_chocolates = 25 # chocolates brought by friend

    total_chocolates = chocolates_in_boxes + chocolates_not_in_box + friend_chocolates
    boxes_needed = (total_chocolates // 15) + 1  # each box can hold 15 chocolates

    # Calculate the number of additional boxes needed
    additional_boxes_needed = boxes_needed - (chocolates_in_boxes // 15) - 3 # Already 3 boxes are filled

    result = additional_boxes_needed
    return result

print(solution())