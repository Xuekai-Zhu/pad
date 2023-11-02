def solution():
    """Nathan has a bouncy ball that bounces to 2/3rds of its starting height with each bounce. If he drops it from the third-floor balcony in the mall, where each story is 24 feet high, how high does the ball go on its second bounce?"""
    starting_height = 24 * 3 # height of third-floor balcony
    bounce_height = starting_height * (2/3) # height of first bounce
    second_bounce_height = bounce_height * (2/3) # height of second bounce
    result = second_bounce_height
    return result

print(solution())