def solution():
    """A charity organization's goal is to distribute 400 boxes of food to a community that was recently destroyed by a flood. Each box contains $80 worth of food and $165 worth of additional supplies such as toiletries and fresh linens. Then, an anonymous donor gives the organization 4 times the amount of money they had already spent, allowing them to pack many more boxes. How many boxes do they pack in total?"""
    # Define the number of boxes and the cost per box
    boxes_goal = 400
    food_cost = 80
    supplies_cost = 165

    # Calculate the initial cost of packing 400 boxes
    initial_cost = boxes_goal * (food_cost + supplies_cost)

    # Calculate the additional cost provided by the donor
    additional_cost = 4 * initial_cost

    # Calculate the number of boxes that can be packed with the additional cost
    total_cost = initial_cost + additional_cost
    total_boxes = total_cost / (food_cost + supplies_cost)

    # return the result
    result = round(total_boxes)
    return result

print(solution())