def solution():
    have_open_toes = True
    completely_cover_feet = False
    is_snowing = True
    if have_open_toes and not completely_cover_feet and is_snowing:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())