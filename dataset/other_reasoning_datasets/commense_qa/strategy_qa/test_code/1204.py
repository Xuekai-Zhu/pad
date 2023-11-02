def solution():
    lunar_surface = "moon"
    cnes_moon_mission = False
    french_flag_planted = False
    if lunar_surface == "moon" and not cnes_moon_mission and french_flag_planted:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())