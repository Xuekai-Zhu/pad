def solution():
    """John decided to start rowing around a square lake. Each side of the lake is 15 miles. Jake can row at twice the speed he can swim. It takes him 20 minutes to swim 1 mile. How long, in hours, does it take to row the lake?"""
    # Define the length of one side of the square lake
    side_length = 15

    # Calculate the distance around the lake
    distance = side_length * 4

    # Calculate Jake's swimming speed
    swimming_speed = 1 / (20/60)  # miles per hour

    # Calculate Jake's rowing speed
    rowing_speed = swimming_speed * 2

    # Calculate the time it takes to row around the lake
    time = distance / rowing_speed  # hours

    # Return the result
    result = time
    return result

print(solution())