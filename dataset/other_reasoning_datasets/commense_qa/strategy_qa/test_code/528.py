def solution():
    crane_domesticated = True
    crane_peck_at_humans = False
    cassowary_aggressive = True
    cassowary_kills = True
    if (crane_domesticated and not crane_peck_at_humans) or (not cassowary_aggressive and not cassowary_kills):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())