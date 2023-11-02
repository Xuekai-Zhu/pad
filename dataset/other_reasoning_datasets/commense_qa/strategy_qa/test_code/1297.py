def solution():
    animated_series = "Hey Arnold"
    character_with_stoop = "Stoop Kid"
    stoop_equivalent = "porch"
    if character_with_stoop and stoop_equivalent in animated_series:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())