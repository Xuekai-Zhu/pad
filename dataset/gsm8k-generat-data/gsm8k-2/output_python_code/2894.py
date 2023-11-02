def solution():
    """Joan wants to visit her family who live 480 miles away. If she drives at a rate of 60 mph and takes a lunch break taking 30 minutes, and 2 bathroom breaks taking 15 minutes each, how many hours did it take her to get there?"""
    distance = 480
    speed = 60
    driving_time = distance / speed
    break_time = (30 + 15 + 15) / 60
    total_time = driving_time + break_time
    result = total_time
    return result

print(solution())