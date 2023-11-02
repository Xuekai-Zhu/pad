def solution():
    has_cactus_spines = True
    uses_CAM = True
    is_aerodynamic = True
    if has_cactus_spines and uses_CAM and is_aerodynamic:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())