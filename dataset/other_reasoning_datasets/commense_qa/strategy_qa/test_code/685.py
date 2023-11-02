def solution():
    flying_fish_habitat = "epipelagic zone"
    well_lit_area = True
    if flying_fish_habitat == "epipelagic zone" and well_lit_area:
        has_good_eyesight = True
    else:
        has_good_eyesight = False
    if has_good_eyesight:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())