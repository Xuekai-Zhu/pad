def solution():
    are_nerve_signals_fired = True
    cause_of_death = "asphyxia"
    if cause_of_death == "asphyxia" and are_nerve_signals_fired:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())