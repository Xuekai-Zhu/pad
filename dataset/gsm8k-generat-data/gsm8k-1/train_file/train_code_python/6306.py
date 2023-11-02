def solution():
    """Michael was watching a TV show, which was aired for 1.5 hours. During this time, there were 3 commercials, which lasted 10 minutes each. How long (in hours) was the TV show itself, not counting commercials?"""
    total_minutes = 90
    commercial_minutes = 3 * 10
    show_minutes = total_minutes - commercial_minutes
    show_hours = show_minutes / 60
    result = show_hours
    return result

print(solution())