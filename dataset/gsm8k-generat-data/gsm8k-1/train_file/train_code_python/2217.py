def solution():
    """Eastern rattlesnakes have 6 segments in their tails, while Western rattlesnakes have 8 segments. What is the percentage difference in their tail size, expressed as a percentage of the Western rattlesnake's tail size?"""
    eastern_tail = 6
    western_tail = 8
    difference = western_tail - eastern_tail
    percent_difference = (difference / western_tail) * 100
    result = percent_difference
    return result

print(solution())