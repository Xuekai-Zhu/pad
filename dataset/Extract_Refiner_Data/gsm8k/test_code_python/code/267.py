def solution():
    
    # Define the number of houses and bedrooms
    num_houses = 2
    num_bedrooms_per_house = 3

    # Define the number of windows per bedroom and the number of windows in each house
    windows_per_bedroom = 2
    windows_per_house = 4

    # Calculate the total number of bedrooms
    total_bedrooms = num_houses * num_bedrooms_per_house

    # Calculate the total number of windows
    total_windows = total_bedrooms * windows_per_bedroom

    # Calculate the number of windows in the house that are not connected to bedrooms
    non_connected_windows = num_houses * (num_bedrooms_per_house - num_bedrooms_per_house)

    # Calculate the total number of windows
    total_windows += non_connected_windows

    # return the result
    result = total_windows
    return result

print(solution())