def solution():
    """Andy is running late. School starts at 8:00 AM and it normally takes him 30 minutes to get there, but today he had to stop for 3 minutes each at 4 red lights and wait 10 minutes to get past construction. If he left his house at 7:15, how many minutes late will he be?"""
    normal_travel_time = 30
    time_lost_at_red_lights = 4 * 3
    time_lost_at_construction = 10
    total_time_lost = time_lost_at_red_lights + time_lost_at_construction
    start_time_hour = 7
    start_time_minute = 15
    start_time = (start_time_hour * 60) + start_time_minute
    arrival_time = start_time + normal_travel_time + total_time_lost
    late_time = arrival_time - (8 * 60)
    result = late_time
    return result

print(solution())