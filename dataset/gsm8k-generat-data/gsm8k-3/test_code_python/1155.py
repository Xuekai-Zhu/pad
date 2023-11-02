def solution():
    """Greta, George and Gloria entered their turtles in the Key West Turtle Race.  Greta’s turtle finished the race in 6 minutes.  George’s turtle finished 2 minutes quicker than Greta’s.  Gloria’s turtle took twice as long as George’s turtle.  How long did it take Gloria’s turtle to finish the race?"""
    # Define the time it took Greta's turtle to finish the race
    greta_time = 6

    # Calculate the time it took George's turtle to finish the race
    george_time = greta_time - 2

    # Calculate the time it took Gloria's turtle to finish the race
    gloria_time = george_time * 2

    # Display the time it took Gloria's turtle to finish the race
    result = gloria_time
    return result

print(solution())