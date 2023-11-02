def solution():
    """There were 28 students inside a bus before stopping at an intersection. After stopping at an intersection, there were 58 students on the bus. What's 40% of the number of students who entered the bus at the intermediate stop?"""
    before_intersection = 28
    after_intersection = 58
    entered_at_intersection = after_intersection - before_intersection
    forty_percent = 0.4 * entered_at_intersection
    result = forty_percent
    return result

print(solution())