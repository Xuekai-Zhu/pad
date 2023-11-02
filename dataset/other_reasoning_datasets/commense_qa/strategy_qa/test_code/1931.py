def solution():
    robert_de_niro_profession = "actor"
    microscope_user = "scientist"
    if microscope_user not in robert_de_niro_profession:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())