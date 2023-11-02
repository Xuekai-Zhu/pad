def solution():
    """If Natasha was going 10 mph over the speed limit and it took her an hour to arrive at her destination that was 60 miles away, what was the speed limit?"""
    distance = 60
    time = 1
    overspeed = 10
    average_speed = distance / time
    speed_limit = average_speed - overspeed
    result = speed_limit
    return result

print(solution())