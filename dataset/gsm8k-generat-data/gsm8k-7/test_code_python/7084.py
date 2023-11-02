def solution():
    total_boxes = 150
    sunday_sales = 1.5  # 50% more than Saturday sales

    # Let x be the number of boxes sold on Saturday
    # Then Sunday sales would be 1.5*x
    # Total sales would be x + 1.5*x = 2.5*x
    # We know total sales is 150, so we can solve for x
    x = total_boxes / 2.5
    saturday_sales = x
    result = saturday_sales
    return result

print(solution())