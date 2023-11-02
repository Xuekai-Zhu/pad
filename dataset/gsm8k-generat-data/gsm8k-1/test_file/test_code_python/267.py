def solution():
    """John has 2 houses with 3 bedrooms each. Each bedroom has 2 windows each. There are an additional 4 windows in each house not connected to bedrooms. How many total windows are there between the houses?"""
    houses = 2
    bedrooms_per_house = 3
    windows_per_bedroom = 2
    extra_windows_per_house = 4
    total_bedrooms = houses * bedrooms_per_house
    bedroom_windows = total_bedrooms * windows_per_bedroom
    extra_windows = houses * extra_windows_per_house
    total_windows = bedroom_windows + extra_windows
    result = total_windows
    return result

print(solution())