def solution():
    sales_goal = 150  # Jill wants to sell at least 150 cookie boxes
    boxes_sold = 5 + 4*5 + (4*5)/2 + 3*((4*5)/2)/2 + 10  # Total number of boxes sold
    boxes_left = sales_goal - boxes_sold  # Boxes left to sell to hit the sales goal
    result = boxes_left
    return result

print(solution())