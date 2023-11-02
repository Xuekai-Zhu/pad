def solution():
    is_sphynx_cat_hairless = True
    is_wool_from_animal_hair = True
    if is_sphynx_cat_hairless and not is_wool_from_animal_hair:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())