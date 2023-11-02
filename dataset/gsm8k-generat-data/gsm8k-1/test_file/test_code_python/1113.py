def solution():
    """The light on a lighthouse blinks 255 times in 5 minutes. How long will it take the light to blink 459 times?"""
    blinks_per_minute = 255 / 5
    time_per_blink = 60 / blinks_per_minute
    time_for_459_blinks = time_per_blink * 459
    result = time_for_459_blinks
    return result

print(solution())