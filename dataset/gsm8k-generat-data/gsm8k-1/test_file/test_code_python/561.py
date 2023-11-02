def solution():
    """Cody and Trevor had 12 sandwiches. Cody ate a third of the sandwiches, and Trevor ate a quarter of the sandwiches. How many sandwiches are left?"""
    total_sandwiches = 12
    cody_eaten = total_sandwiches / 3
    trevor_eaten = total_sandwiches / 4
    sandwiches_left = total_sandwiches - cody_eaten - trevor_eaten
    result = sandwiches_left
    return result

print(solution())