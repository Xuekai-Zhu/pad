def solution():
    """Hugo can fold a small box in 3 seconds and a medium one in twice that time. Tom can fold both the small and medium boxes in 4 seconds. If Hugo and Tom want to leave as early as possible, how long (in seconds) will it take them to fold 2400 small boxes and 1800 medium boxes?"""
    hugo_small_time = 3
    hugo_medium_time = 6
    tom_small_time = 4
    tom_medium_time = 4

    # time for Hugo to fold all small boxes
    total_hugo_small_time = hugo_small_time * 2400

    # time for Hugo to fold all medium boxes
    total_hugo_medium_time = hugo_medium_time * 1800

    # time for Tom to fold all small and medium boxes
    total_tom_time = tom_small_time * 2400 + tom_medium_time * 1800

    # find the minimum time by choosing the faster option
    if total_hugo_small_time + total_hugo_medium_time < total_tom_time:
        result = total_hugo_small_time + total_hugo_medium_time
    else:
        result = total_tom_time

    return result

print(solution())