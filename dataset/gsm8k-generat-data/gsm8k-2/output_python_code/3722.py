def solution():
    """Cameron drives at twice the speed of his brother, Chase. But Danielle drives at three times the speed of Cameron. If it takes Danielle 30 minutes to travel from Granville to Salisbury, how long, in minutes, will it take Chase to travel from Granville to Salisbury?"""
    danielle_speed = 3
    cameron_speed = danielle_speed / 3
    chase_speed = cameron_speed / 2
    danielle_time = 30
    granville_to_salisbury_distance = 1
    chase_time = granville_to_salisbury_distance / chase_speed * 60
    result = chase_time
    return result

print(solution())