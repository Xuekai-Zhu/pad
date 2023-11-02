def solution():
    """Cameron drives at twice the speed of his brother, Chase. But Danielle drives at three times the speed of Cameron. If it takes Danielle 30 minutes to travel from Granville to Salisbury, how long, in minutes, will it take Chase to travel from Granville to Salisbury?"""
    # Let's assume Cameron's speed is x
    # Then, Chase's speed is x/2
    # Danielle's speed is 3x

    # Let's assume the distance from Granville to Salisbury is d
    # Then, Danielle's time taken to travel is d/3x = 30 minutes

    # Solving for x, we get:
    x = d/90

    # Time taken for Chase to travel the same distance at half the speed of Cameron is:
    chase_time_taken = d/(x/2)
    
    result = chase_time_taken * 60 # Convert to minutes
    return result

print(solution())