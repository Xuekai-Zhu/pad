def solution():
    """A charity organization's goal is to distribute 400 boxes of food to a community that was recently destroyed by a flood. Each box contains $80 worth of food and $165 worth of additional supplies such as toiletries and fresh linens. Then, an anonymous donor gives the organization 4 times the amount of money they had already spent, allowing them to pack many more boxes. How many boxes do they pack in total?"""
    boxes_goal = 400
    food_cost = 80
    supplies_cost = 165
    total_cost = food_cost + supplies_cost
    initial_cost = boxes_goal * total_cost
    additional_money = initial_cost * 4
    total_boxes = (initial_cost + additional_money) // total_cost
    result = total_boxes
    return result

print(solution())