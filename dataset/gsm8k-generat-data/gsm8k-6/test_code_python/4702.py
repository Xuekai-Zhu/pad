def solution():
    kelly_time = 3   # time in minutes
    brittany_time = (kelly_time * 60) - 20  # convert to seconds and subtract 20 seconds
    buffy_time = (brittany_time - 40)  # subtract 40 seconds
    result = buffy_time
    return result

print(solution())