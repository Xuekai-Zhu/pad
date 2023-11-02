def solution():
    """Two athletes decided to compete to see who had the best jumping ability. They were each going to do the long jump, triple jump, and high jump to see who had the highest average jump. The first athlete jumped 26 feet in the long jump, 30 feet in the triple jump, and 7 feet in the high jump. The second athlete jumped 24 feet in the long jump, 34 feet in the triple jump, and 8 feet in the high jump. What was the average jump of the winner?"""
    athlete1_total = 26 + 30 + 7
    athlete2_total = 24 + 34 + 8
    athlete1_average = athlete1_total / 3
    athlete2_average = athlete2_total / 3
    if athlete1_average > athlete2_average:
        result = athlete1_average
    else:
        result = athlete2_average
    return result

print(solution())