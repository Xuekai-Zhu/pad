def solution():
    """Tom paints a room that has 5 walls.  Each wall is 2 meters by 3 meters.  John can paint 1 square meter every 10 minutes.  He has 10 hours to paint everything.  How many hours does he have to spare?"""
    # Define the dimensions of each wall
    wall_width = 2
    wall_height = 3

    # Calculate the area of each wall
    wall_area = wall_width * wall_height

    # Calculate the total area of all 5 walls
    total_area = wall_area * 5

    # Define John's painting rate in square meters per minute
    painting_rate = 1 / 10  # 1 square meter in 10 minutes

    # Calculate the time needed to paint everything in minutes
    painting_time = total_area / painting_rate

    # Convert the painting time to hours
    painting_time_hours = painting_time / 60

    # Calculate the spare time in hours
    spare_time_hours = 10 - painting_time_hours

    # Display the spare time
    result = spare_time_hours
    return result

print(solution())