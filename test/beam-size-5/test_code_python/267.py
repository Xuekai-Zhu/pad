def solution():
    num_houses = 2
    num_bedrooms_per_house = 3
    num_windows_per_bedroom = 2
    num_windows_not_connected_per_house = 4

    # Calculate the total number of bedrooms
    total_bedrooms = num_houses * num_bedrooms_per_house

    # Calculate the total number of windows in all bedrooms
    total_bedrooms_windows = num_bedrooms * num_windows_per_bedroom

    # Calculate the total number of windows not connected to bedrooms
    total_not_connected_windows = num_houses * num_windows_not_connected_per_house

    # Calculate the total number of windows between all houses
    total_windows = total_bedrooms_windows + total_not_connected_windows
    result = total_windows
    return result

print(solution())