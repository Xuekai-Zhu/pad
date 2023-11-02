def solution():
    """Joan wants to visit her family who live 480 miles away. If she drives at a rate of 60 mph and takes a lunch break taking 30 minutes, and 2 bathroom breaks taking 15 minutes each, how many hours did it take her to get there?"""
    distance = 480
    rate = 60
    lunch_break = 0.5
    bathroom_breaks = 0.5
    drive_time = distance / rate
    total_breaks = lunch_break + (2 * bathroom_breaks)
    total_time = drive_time + total_breaks
    result = total_time
    return result

print(solution())