def solution():
    """Michelangelo has 28 ceilings to paint. This week, he paints 12 of them. Next week, he will paint 1/4 the number of ceilings he did this week. How many ceilings will be left to paint after next week?"""
    ceilings_to_paint = 28
    painted_this_week = 12
    painted_next_week = painted_this_week * (1/4)
    remaining_paint = ceilings_to_paint - painted_this_week - painted_next_week
    result = remaining_paint
    return result

print(solution())