def solution():
    """Greta, George and Gloria entered their turtles in the Key West Turtle Race. Greta’s turtle finished the race in 6 minutes. George’s turtle finished 2 minutes quicker than Greta’s. Gloria’s turtle took twice as long as George’s turtle. How long did it take Gloria’s turtle to finish the race?"""
    # Define Greta's time as 6 minutes
    greta_time = 6

    # Define George's time as Greta's time minus 2 minutes
    george_time = greta_time - 2

    # Define Gloria's time as twice George's time
    gloria_time = george_time * 2

    # Return Gloria's time
    result = gloria_time
    return result

print(solution())