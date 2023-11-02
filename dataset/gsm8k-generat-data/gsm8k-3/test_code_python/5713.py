def solution():
    """Tony can run a mile twice as fast as Tina, who with a time of 6 minutes is one-third as fast a runner as Tom.  What are all three of their mile times when added together?"""
    # Let Tom's time be t
    t = 6 / (1/3) # Tina is 1/3 as fast as Tom
    # Tina's time is three times longer than Tom's time:
    tina_time = t * 3 
    # Tony is twice as fast as Tina:
    tony_time = tina_time / 2 
    # The total time is the sum of their times:
    total_time = t + tina_time + tony_time

    # Display the total time
    result = total_time
    return result

print(solution())