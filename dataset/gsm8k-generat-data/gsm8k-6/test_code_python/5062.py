def solution():
    # Let's assume there are n rooms with 2 windows
    # Then, the total number of windows in those rooms would be 2n
    # From the given information, we know that there are 5 rooms with 4 windows and 8 rooms with 3 windows
    # So the total number of windows in those rooms would be 5*4 + 8*3 = 37
    # Therefore, the total number of windows in rooms with 2 windows would be 122-37 = 85
    # And since each room with 2 windows contributes 2 windows, the number of rooms with 2 windows would be 85/2 = 42.5
    # But since the number of rooms must be a whole number, we take the floor of 42.5 which is 42
    result = 42
    return result

print(solution())