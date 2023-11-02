def solution():
    feet_per_rung = 18
    inches_per_foot = 12
    rung_spacing = 6
    total_rungs = (50 * inches_per_foot) / (feet_per_rung + rung_spacing)
    total_feet = total_rungs * feet_per_rung
    result = total_feet
    return result

print(solution())