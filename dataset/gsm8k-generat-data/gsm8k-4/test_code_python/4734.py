def solution():
    """In a classroom, there are blue chairs, green chairs, and white chairs. There are 10 blue chairs. The green chairs are 3 times as many as the blue chairs, and there are 13 fewer white chairs than the green and blue chairs combined. How many chairs are there in a classroom?"""
    # Define the number of blue chairs
    blue_chairs = 10

    # Calculate the number of green chairs
    green_chairs = blue_chairs * 3

    # Calculate the total number of blue and green chairs
    blue_and_green = blue_chairs + green_chairs

    # Calculate the number of white chairs
    white_chairs = blue_and_green - 13

    # Calculate the total number of chairs
    total_chairs = blue_chairs + green_chairs + white_chairs

    # Return the result
    result = total_chairs
    return result

print(solution())