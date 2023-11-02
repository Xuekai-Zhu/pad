def solution():
    want_to_gain_weight = True
    coca_leaves_suppress_hunger = True
    if want_to_gain_weight and not coca_leaves_suppress_hunger:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())