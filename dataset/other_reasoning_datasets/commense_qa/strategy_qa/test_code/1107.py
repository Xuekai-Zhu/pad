def solution():
    sesame_seed_shelf_life = "6-12 months"
    white_rice_shelf_life = "4-5 years"
    if white_rice_shelf_life < sesame_seed_shelf_life:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())