def solution():
    """Nida has 50 chocolates in which some are in 3 filled boxes and 5 pieces are not in a box. Her friend brought 25 pieces of chocolates. If all chocolates must be placed in a box, how many more boxes do they need?"""
    chocolates_in_boxes = 3 * 3
    chocolates_not_in_box = 5
    chocolates_total = 50 + 25
    chocolates_to_box = chocolates_total - chocolates_in_boxes - chocolates_not_in_box
    boxes_needed = chocolates_to_box // 3 + (1 if chocolates_to_box % 3 != 0 else 0) # round up to nearest box
    result = boxes_needed
    return result

print(solution())