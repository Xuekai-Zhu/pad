def solution():
    """Diana needs to bike 10 miles to get home. She can bike 3 mph for two hours before she gets tired, and she can bike 1 mph until she gets home. How long will it take Diana to get home?"""
    distance = 10
    speed1 = 3
    time1 = 2
    speed2 = 1
    time2 = (distance - speed1 * time1) / speed2
    total_time = time1 + time2
    result = total_time
    return result

print(solution())