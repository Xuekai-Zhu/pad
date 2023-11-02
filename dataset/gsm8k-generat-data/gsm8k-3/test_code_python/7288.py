def solution():
    """A boat is traveling across a square lake at 10 MPH. It takes 2 hours to go across the length of the lake. It then travels the whole width of the lake at the same speed, which takes 30 minutes. How many square miles is the lake?"""
    # Define the speed of the boat
    SPEED = 10

    # Calculate the length of the lake
    length = SPEED * 2

    # Calculate the width of the lake
    width = SPEED * 0.5

    # Calculate the area of the lake
    area = length * width

    # Display the area of the lake
    result = area
    return result

print(solution())