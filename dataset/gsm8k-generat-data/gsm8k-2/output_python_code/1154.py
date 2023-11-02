def solution():
    """Greta, George and Gloria entered their turtles in the Key West Turtle Race. Greta’s turtle finished the race in 6 minutes. George’s turtle finished 2 minutes quicker than Greta’s. Gloria’s turtle took twice as long as George’s turtle. How long did it take Gloria’s turtle to finish the race?"""
    greta_time = 6
    george_time = greta_time - 2
    gloria_time = george_time * 2
    result = gloria_time
    return result

print(solution())