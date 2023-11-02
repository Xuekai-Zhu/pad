def solution():
    seismophobia = True
    located_far_from_tectonic_plates = True
    if located_far_from_tectonic_plates and not seismophobia:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())