def solution():
    """Every room in a building has at least two windows and a maximum of 4 windows. There are 122 windows total. If 5 rooms have 4 windows and 8 rooms have 3 windows, how many rooms in the building have 2 windows?"""
    # Define the number of rooms with 4 windows and 3 windows
    rooms_with_4_windows = 5
    rooms_with_3_windows = 8

    # Define the total number of windows in those rooms
    total_windows_4 = rooms_with_4_windows * 4
    total_windows_3 = rooms_with_3_windows * 3

    # Define the total number of windows in the entire building
    total_windows = 122

    # Calculate the number of windows in rooms with 2 windows
    windows_with_2 = total_windows - total_windows_4 - total_windows_3

    # Calculate the number of rooms with 2 windows
    rooms_with_2_windows = windows_with_2 / 2

    # Return the result
    result = int(rooms_with_2_windows)
    return result

print(solution())