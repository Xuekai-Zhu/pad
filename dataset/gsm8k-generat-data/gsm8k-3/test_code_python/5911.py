def solution():
    """A building has 20 floors. Each floor is 3 meters high, except for the last two floors. The last two floors are each 0.5 meters higher. How tall is the building?"""
    # Define the height of each regular floor
    REGULAR_FLOOR_HEIGHT = 3

    # Define the height of each of the last two floors
    LAST_FLOOR_HEIGHT = REGULAR_FLOOR_HEIGHT + 0.5

    # Define the number of regular floors
    num_regular_floors = 18

    # Calculate the height of the regular floors
    regular_floor_height = num_regular_floors * REGULAR_FLOOR_HEIGHT

    # Calculate the height of the last two floors
    last_floor_height = 2 * LAST_FLOOR_HEIGHT

    # Calculate the total height of the building
    total_height = regular_floor_height + last_floor_height

    # Display the total height of the building
    result = total_height
    return result

print(solution())