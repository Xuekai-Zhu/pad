def solution():
    """Cameron drives at twice the speed of his brother, Chase. But Danielle drives at three times the speed of Cameron. If it takes Danielle 30 minutes to travel from Granville to Salisbury, how long, in minutes, will it take Chase to travel from Granville to Salisbury?"""
    cameron_speed = 2
    chase_speed = 1
    danielle_speed = 3
    danielle_time = 30
    cameron_time = danielle_time * (cameron_speed / danielle_speed)
    chase_time = cameron_time * (chase_speed / cameron_speed)
    result = round(chase_time)
    return result

print(solution())