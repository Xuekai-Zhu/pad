def solution():
    holy_land_revered_by = ["Jews", "Muslims", "Christians"]
    earliest_presence_in_holy_land = 3500
    adamu_tribe_presence = 2600
    if adamu_tribe_presence >= earliest_presence_in_holy_land:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())