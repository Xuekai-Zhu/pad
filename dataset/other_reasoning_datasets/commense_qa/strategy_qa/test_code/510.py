def solution():
    cattle_slaughtered_for_leather = True
    leather_used_to_make_drums = True
    if cattle_slaughtered_for_leather and leather_used_to_make_drums:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())