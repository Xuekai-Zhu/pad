def solution():
    """William left Missouri by 7:00 AM and arrived at his hometown by 8:00 PM. He had 3 stops of 25, 10 and 25 minutes respectively during the journey. How many hours did he spend on the road?"""
    start_time = 7
    end_time = 20
    total_travel_time = (end_time - start_time) * 60
    total_stop_time = 25 + 10 + 25
    actual_travel_time = total_travel_time - total_stop_time
    hours_on_road = actual_travel_time / 60
    result = hours_on_road
    return result

print(solution())