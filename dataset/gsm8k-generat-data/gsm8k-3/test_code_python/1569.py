def solution():
    """John decided to start rowing around a square lake.  Each side of the lake is 15 miles.  Jake can row at twice the speed he can swim.  It takes him 20 minutes to swim 1 mile.  How long, in hours, does it take to row the lake?"""
    # Define the length of each side of the lake in miles
    SIDE_LENGTH = 15

    # Calculate the distance around the lake in miles
    distance = 4 * SIDE_LENGTH

    # Calculate Jake's swimming speed in miles per hour
    swim_speed = 60 / (20 / 60)  # 1 mile in 20 minutes is 3 miles per hour

    # Calculate Jake's rowing speed in miles per hour
    row_speed = swim_speed * 2

    # Calculate the time it will take Jake to row around the lake in hours
    time = distance / row_speed

    # Display the time it will take Jake to row around the lake
    result = time
    return result

print(solution())