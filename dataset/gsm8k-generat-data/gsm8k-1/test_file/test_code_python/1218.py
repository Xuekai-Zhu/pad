def solution():
    """Luke is buying fabric for new curtains. There are five windows. Each window is 35 inches wide and Luke needs to buy fabric equal to 2 times the total width of the windows. How much fabric should he buy?"""
    windows = 5
    width_per_window = 35
    total_width = windows * width_per_window
    fabric_needed = total_width * 2
    result = fabric_needed
    return result

print(solution())