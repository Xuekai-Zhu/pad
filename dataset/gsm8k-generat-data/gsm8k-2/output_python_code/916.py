def solution():
    """Jason is climbing a telephone pole next to a tree his friend Matt is climbing. Matt can climb 6 feet/minute and Jason can climb 12 feet per minute. After 7 minutes, how much higher will Jason be than Matt?"""
    matt_height = 6 * 7
    jason_height = 12 * 7
    height_difference = jason_height - matt_height
    result = height_difference
    return result

print(solution())