def solution():
    boxes = 400  # The organization's goal is to distribute 400 boxes of food
    food_value = 80  # Each box contains $80 worth of food
    supply_value = 165  # Each box contains $165 worth of additional supplies

    # Calculate the cost of each box
    box_cost = food_value + supply_value

    # Calculate the total cost of distributing 400 boxes
    total_cost = box_cost * boxes

    # Calculate the amount of money the anonymous donor gave to the organization
    additional_money = total_cost * 4

    # Calculate the total cost of distributing all the boxes with the additional money
    total_cost_with_additional_money = total_cost + additional_money

    # Calculate the number of boxes the organization can pack with the additional money
    total_boxes = total_cost_with_additional_money / box_cost
    result = total_boxes
    return result

print(solution())