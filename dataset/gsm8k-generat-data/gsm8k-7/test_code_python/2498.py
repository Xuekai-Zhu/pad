def solution():
    num_nuggets = 100
    nuggets_per_box = 20
    cost_per_box = 4.0

    # Calculate the total number of boxes of chicken nuggets that Mark needs to buy
    num_boxes = num_nuggets / nuggets_per_box

    # Round up to the nearest whole box
    num_boxes = math.ceil(num_boxes)

    # Calculate the total cost of all boxes of chicken nuggets that Mark needs to buy
    total_cost = num_boxes * cost_per_box
    result = total_cost
    return result

print(solution())