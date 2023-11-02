def solution():
    can_see_full_circle = False
    sun_at_midday = True
    closer_to_horizon = True
    if sun_at_midday and closer_to_horizon:
        can_see_full_circle = True
    if can_see_full_circle:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())