def solution():
    
    ceilings_to_paint = 28
    painted_this_week = 12
    painted_next_week = painted_this_week * (1/4)
    remaining_paint = ceilings_to_paint - painted_this_week - painted_next_week
    result = remaining_paint
    return result

print(solution())