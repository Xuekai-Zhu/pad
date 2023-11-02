def solution():
    """Rob and Mark plan to meet at the national park. It takes 1 hour for Rob to get to the national park and it takes three times as much time for Mark to get to the national park. If Rob leaves his home at 11 a.m., at what time should Mark leave his home so that they both arrive at the same time?"""
    rob_time = 1
    mark_time = 3 * rob_time
    rob_departure = 11
    mark_departure = rob_departure - mark_time
    result = mark_departure
    return result

print(solution())