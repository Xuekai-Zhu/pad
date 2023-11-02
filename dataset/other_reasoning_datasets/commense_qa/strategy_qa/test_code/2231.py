def solution():
    white_blood_cells_protect_against_disease = True
    disease_can_kill = True
    if not white_blood_cells_protect_against_disease and disease_can_kill:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())