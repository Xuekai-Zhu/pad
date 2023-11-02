def solution():
    eastern_orthodox_calendar_use = [691, 1728]
    byzantine_empire_calendar_use = [988, 1453]
    overlap = max(min(eastern_orthodox_calendar_use[1], byzantine_empire_calendar_use[1]) -
                  max(eastern_orthodox_calendar_use[0], byzantine_empire_calendar_use[0]), 0)
    if overlap > 0:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())