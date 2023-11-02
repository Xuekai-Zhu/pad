def solution():
    """Roger had a 6-hour drive planned out. He didn't want to listen to music so he downloaded several podcasts. The first podcast was 45 minutes long. The second podcast was twice as long as that. The third podcast was 1 hour and 45 minutes long. His fourth podcast is 1 hour long. How many hours will his next podcast have to be to fill up the full 6 hours?"""
    total_time = 6 * 60  # convert to minutes
    current_time = 45 + 2 * 45 + 1 * 60 + 1 * 60  # add up the time of the 4 podcasts
    remaining_time = total_time - current_time  # calculate the remaining time
    next_podcast_time = remaining_time  # the next podcast will have to fill up the remaining time
    result = next_podcast_time / 60  # convert back to hours
    return result

print(solution())