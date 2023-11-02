def solution():
    """Brian has twice as many tennis balls as Frodo, who has 8 more than Lily. If Lily has 3 tennis balls, how many does Brian have?"""
    # Define the number of tennis balls Lily has
    lily_balls = 3

    # Calculate the number of balls Frodo has
    frodo_balls = lily_balls + 8

    # Calculate the number of balls Brian has
    brian_balls = frodo_balls * 2

    result = brian_balls
    return result

print(solution())