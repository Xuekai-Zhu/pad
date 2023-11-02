def solution():
    """Andy is running late. School starts at 8:00 AM and it normally takes him 30 minutes to get there, but today he had to stop for 3 minutes each at 4 red lights and wait 10 minutes to get past construction. If he left his house at 7:15, how many minutes late will he be?"""
    departure_time = 7.25
    total_extra_time = (3 * 4) + 10
    total_travel_time = 30 + total_extra_time
    arrival_time = departure_time + (total_travel_time / 60)
    late_time = arrival_time - 8
    result = late_time * 60
    return result

print(solution())