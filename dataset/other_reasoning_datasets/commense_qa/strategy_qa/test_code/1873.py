def solution():
    broom_design = "curling"
    traditional_head = False
    costly_to_replace = True
    if broom_design == "curling" and not traditional_head and costly_to_replace:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())