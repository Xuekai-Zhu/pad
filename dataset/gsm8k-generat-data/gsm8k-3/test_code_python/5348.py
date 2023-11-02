def solution():
    """There are 12 inches to a foot. Blossom measures her room and finds that it is exactly 10 feet long in each direction. In square inches, what is the area of her room?"""
    # Define the number of inches in a foot
    INCHES_PER_FOOT = 12

    # Define the length and width of the room in feet
    length = 10
    width = 10

    # Calculate the area of the room in square feet
    area_feet = length * width

    # Convert the area to square inches
    area_inches = area_feet * INCHES_PER_FOOT ** 2

    # Display the area of the room in square inches
    result = area_inches
    return result

print(solution())