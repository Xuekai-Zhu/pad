def solution():
    # Define variables for Carlos Ghosn's current legal situation
    is_ceo_of_nissan = True
    has_red_notice_on_interpol = True
    is_wanted_fugitive = False
    if is_ceo_of_nissan and has_red_notice_on_interpol:
        is_wanted_fugitive = True
    if is_wanted_fugitive:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())