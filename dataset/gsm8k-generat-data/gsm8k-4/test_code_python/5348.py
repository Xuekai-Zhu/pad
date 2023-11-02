def solution():
    """There are 12 inches to a foot. Blossom measures her room and finds that it is exactly 10 feet long in each direction. In square inches, what is the area of her room?"""
    # Define the number of inches in a foot
    INCHES_PER_FOOT = 12

    # Define the dimensions of the room in feet
    length = 10
    width = 10

    # Convert the dimensions of the room to inches
    length_inches = length * INCHES_PER_FOOT
    width_inches = width * INCHES_PER_FOOT

    # Calculate the area of the room in square inches
    area = length_inches * width_inches

    # return the result
    result = area
    return result

print(solution())