def solution():
    # Calculate the total number of chocolates
    total_chocolates = 50 + 25

    # Calculate the number of chocolates already in boxes
    chocolates_in_boxes = 3 * 3

    # Calculate the remaining number of chocolates
    remaining_chocolates = total_chocolates - chocolates_in_boxes - 5

    # Calculate the number of boxes needed for the remaining chocolates
    boxes_needed = ((remaining_chocolates - 1) // 4) + 1

    result = boxes_needed
    return result

print(solution())