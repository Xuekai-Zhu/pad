def solution():
    """John starts climbing a very steep hill.  He travels 1 foot vertically for every two feet horizontally.  His elevation increases from 100 feet to 1450 feet.  How far does he move horizontally, in feet?"""
    # Define the initial and final elevations
    initial_elevation = 100
    final_elevation = 1450

    # Calculate the change in elevation
    elevation_change = final_elevation - initial_elevation

    # Calculate the corresponding horizontal distance traveled
    horizontal_distance = 2 * elevation_change

    # Return the horizontal distance traveled
    result = horizontal_distance
    return result

print(solution())