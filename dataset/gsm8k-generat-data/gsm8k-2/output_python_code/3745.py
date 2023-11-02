def solution():
    """A pen and pencil have a total cost of $6. If the pen costs twice as much as the pencil, what is the cost of the pen?"""
    total_cost = 6
    pen_cost = 0
    for i in range(1, total_cost):
        if i * 2 + i == total_cost:
            pen_cost = i * 2
    result = pen_cost
    return result

print(solution())