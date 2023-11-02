def solution():
    """Tony can run a mile twice as fast as Tina, who with a time of 6 minutes is one-third as fast a runner as Tom. What are all three of their mile times when added together?"""
    # Let x be Tom's mile time in minutes
    x = None

    # Tina is one-third as fast as Tom, so her mile time is 3 times longer
    tina_time = 18

    # Tony can run a mile twice as fast as Tina
    tony_time = tina_time / 2

    # The total mile time for all three runners
    total_time = x + tina_time + tony_time

    # Return the result
    result = total_time
    return result

print(solution())