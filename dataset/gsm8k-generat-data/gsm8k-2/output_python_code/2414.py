def solution():
    """There were some snowflakes at first. It snowed an additional 4 snowflakes every 5 minutes. If there were 58 snowflakes after 1 hour, how many snowflakes were there at first?"""
    initial_snowflakes = 58 - (4 * 11)  # 11 sets of 4 snowflakes added over 55 minutes
    result = initial_snowflakes
    return result

print(solution())