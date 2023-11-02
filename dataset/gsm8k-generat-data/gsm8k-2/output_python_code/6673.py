def solution():
    """William left Missouri by 7:00 AM and arrived at his hometown by 8:00 PM. He had 3 stops of 25, 10 and 25 minutes respectively during the journey. How many hours did he spend on the road?"""
    total_travel_time = 13 * 60  # convert to minutes
    total_stop_time = 25 + 10 + 25
    total_time = total_travel_time + total_stop_time
    hours_on_road = total_time / 60
    result = hours_on_road
    return result

print(solution())