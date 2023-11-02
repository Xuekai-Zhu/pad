def solution():
    """Nida has 50 chocolates in which some are in 3 filled boxes and 5 pieces are not in a box. Her friend brought 25 pieces of chocolates. If all chocolates must be placed in a box, how many more boxes do they need?"""
    chocolates_in_boxes = 3 * 3 # 3 filled boxes with 3 chocolates each
    chocolates_not_in_box = 5
    total_chocolates = chocolates_in_boxes + chocolates_not_in_box
    friend_chocolates = 25
    total_chocolates += friend_chocolates
    boxes_needed = total_chocolates // 3 # Each box can hold 3 chocolates
    extra_boxes_needed = boxes_needed - 3 # Nida already has 3 filled boxes
    result = extra_boxes_needed
    return result

print(solution())