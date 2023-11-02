def solution():
    """Tony can run a mile twice as fast as Tina, who with a time of 6 minutes is one-third as fast a runner as Tom. What are all three of their mile times when added together?"""
    tina_time = 6
    tom_time = tina_time / (1/3)
    tony_time = tina_time / 2
    total_time = tina_time + tom_time + tony_time
    result = total_time
    return result

print(solution())