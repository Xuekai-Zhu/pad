def solution():
    red_blood_cells_fraction = 0.45
    white_blood_cells_fraction = 0.01
    if white_blood_cells_fraction > red_blood_cells_fraction:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())