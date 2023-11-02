def solution():
    """A charity organization's goal is to distribute 400 boxes of food to a community that was recently destroyed by a flood. Each box contains $80 worth of food and $165 worth of additional supplies such as toiletries and fresh linens. Then, an anonymous donor gives the organization 4 times the amount of money they had already spent, allowing them to pack many more boxes. How many boxes do they pack in total?"""
    num_boxes = 400
    box_cost = 80 + 165
    total_cost = num_boxes * box_cost
    donated_amount = total_cost * 4
    total_boxes = (donated_amount + total_cost) // box_cost
    result = total_boxes
    return result

print(solution())