def solution():
    """Michelangelo has 28 ceilings to paint. This week, he paints 12 of them. Next week, he will paint 1/4 the number of ceilings he did this week. How many ceilings will be left to paint after next week?"""
    total_ceilings = 28
    painted_this_week = 12
    painted_next_week = painted_this_week * (1/4)
    total_painted = painted_this_week + painted_next_week
    remaining_ceilings = total_ceilings - total_painted
    result = remaining_ceilings
    return result

print(solution())