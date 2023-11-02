def solution():
    """Every room in a building has at least two windows and a maximum of 4 windows. There are 122 windows total. If 5 rooms have 4 windows and 8 rooms have 3 windows, how many rooms in the building have 2 windows?"""
    total_windows = 122
    rooms_with_four = 5
    rooms_with_three = 8
    windows_with_four = rooms_with_four * 4
    windows_with_three = rooms_with_three * 3
    windows_with_two = total_windows - windows_with_four - windows_with_three
    rooms_with_two = windows_with_two / 2
    result = rooms_with_two
    return result

print(solution())