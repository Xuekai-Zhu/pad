def solution():
    """Roger had a 6-hour drive planned out. He didn't want to listen to music so he downloaded several podcasts.
    The first podcast was 45 minutes long. The second podcast was twice as long as that. The third podcast was 1 hour and 45 minutes long.
    His fourth podcast is 1 hour long. How many hours will his next podcast have to be to fill up the full 6 hours?"""
    total_minutes = 6 * 60
    podcast_minutes = 45 + (2 * 45) + (1 * 60) + (1 * 60)
    minutes_left = total_minutes - podcast_minutes
    hours_left = minutes_left / 60
    result = hours_left
    return result

print(solution())