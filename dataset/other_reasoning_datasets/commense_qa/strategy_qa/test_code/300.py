def solution():
    drag_kings_use_makeup = True
    testosterone_is_prescribed_for_transgender_men = True
    drag_kings_identify_as_women = True
    if drag_kings_use_makeup and testosterone_is_prescribed_for_transgender_men and not drag_kings_identify_as_transgender:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())