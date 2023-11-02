def solution():
    """Brian has twice as many tennis balls as Frodo, who has 8 more than Lily. If Lily has 3 tennis balls, how many does Brian have?"""
    # Define Lily's number of tennis balls
    lily_balls = 3

    # Calculate Frodo's number of tennis balls
    frodo_balls = lily_balls + 8

    # Calculate Brian's number of tennis balls
    brian_balls = frodo_balls * 2

    # Display Brian's number of tennis balls
    result = brian_balls
    return result

print(solution())