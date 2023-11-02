def solution():
    writing_material = "parchment"
    animal_skin_used = True
    PETA_offended = True
    if writing_material == "parchment" and animal_skin_used and PETA_offended:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())