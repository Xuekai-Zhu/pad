def solution():
    modafinil_dose = 200
    lethal_dose = 5000
    if lethal_dose / modafinil_dose >= 25:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())