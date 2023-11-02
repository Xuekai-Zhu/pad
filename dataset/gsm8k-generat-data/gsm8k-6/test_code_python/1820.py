def solution():
    chocolates_in_boxes = 50 - 5  # chocolates in 3 filled boxes
    total_chocolates = chocolates_in_boxes + 25  # total number of chocolates after friend brought more
    boxes_needed = (total_chocolates // 12) + 1  # each box holds 12 chocolates, add 1 for leftover chocolates
    boxes_needed -= 3  # accounted for 3 filled boxes already
    result = boxes_needed
    return result

print(solution())