def solution():
    """Jason is climbing a telephone pole next to a tree his friend Matt is climbing. Matt can climb 6 feet/minute and Jason can climb 12 feet per minute. After 7 minutes, how much higher will Jason be than Matt?"""
    matt_climbs = 6 * 7
    jason_climbs = 12 * 7
    height_diff = jason_climbs - matt_climbs
    result = height_diff
    return result

print(solution())