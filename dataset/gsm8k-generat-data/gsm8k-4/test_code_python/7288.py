def solution():
    """A boat is traveling across a square lake at 10 MPH. It takes 2 hours to go across the length of the lake. It then travels the whole width of the lake at the same speed, which takes 30 minutes. How many square miles is the lake?"""
    # Define the speed of the boat
    SPEED = 10

    # Convert 2 hours to minutes
    time_length = 2*60

    # Calculate the length of the lake
    length = SPEED * (time_length / 60)

    # Convert 30 minutes to hours
    time_width = 0.5

    # Calculate the width of the lake
    width = SPEED * time_width

    # Calculate the area of the lake
    area = length * width

    # Return the result
    result = area
    return result

print(solution())