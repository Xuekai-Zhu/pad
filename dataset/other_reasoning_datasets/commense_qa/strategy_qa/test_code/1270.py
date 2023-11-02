def solution():
    mozambique_drill = "two shots to the body and one to the head"
    ranger_gun = "M4A1"
    ranger_gun_range = 600
    if mozambique_drill == "easy" and ranger_gun_range >= 10:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())