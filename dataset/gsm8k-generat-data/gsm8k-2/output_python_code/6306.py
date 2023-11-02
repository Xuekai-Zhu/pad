def solution():
    """Michael was watching a TV show, which was aired for 1.5 hours. During this time, there were 3 commercials, which lasted 10 minutes each. How long (in hours) was the TV show itself, not counting commercials?"""
    total_show_time = 1.5
    commercial_time = 3 * 10 / 60
    show_time = total_show_time - commercial_time
    result = show_time
    return result

print(solution())