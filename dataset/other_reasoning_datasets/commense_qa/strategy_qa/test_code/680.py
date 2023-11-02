def solution():
    vampire_weakness = "garlic"
    chive_variant = "garlic chives"
    if vampire_weakness in chive_variant:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())