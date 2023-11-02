def solution():
    """Tom paints a room that has 5 walls. Each wall is 2 meters by 3 meters. John can paint 1 square meter every 10 minutes. He has 10 hours to paint everything. How many hours does he have to spare?"""
    
    # calculate the area of each wall (in square meters)
    wall_area = 2 * 3
    total_wall_area = wall_area * 5

    # calculate the total time needed to paint all the walls (in minutes)
    total_time = total_wall_area * 10

    # convert the time to hours and subtract from the 10 hour deadline
    hours_left = (10 * 60 - total_time) / 60

    return hours_left

print(solution())