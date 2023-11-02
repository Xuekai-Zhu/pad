def solution():
    """Every room in a building has at least two windows and a maximum of 4 windows. There are 122 windows total. If 5 rooms have 4 windows and 8 rooms have 3 windows, how many rooms in the building have 2 windows?"""
    # Define the number of rooms with 4 windows and 3 windows
    num_rooms_4_windows = 5
    num_rooms_3_windows = 8

    # Calculate the total number of windows in the rooms with 4 windows
    total_windows_4 = num_rooms_4_windows * 4

    # Calculate the total number of windows in the rooms with 3 windows
    total_windows_3 = num_rooms_3_windows * 3

    # Calculate the total number of rooms in the building
    total_rooms = num_rooms_4_windows + num_rooms_3_windows + (122 - total_windows_4 - total_windows_3) // 2

    # Display the number of rooms with 2 windows
    result = total_rooms - num_rooms_4_windows - num_rooms_3_windows
    return result

print(solution())