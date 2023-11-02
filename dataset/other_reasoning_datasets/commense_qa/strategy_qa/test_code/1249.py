def solution():
    seroquel_for_bipolar = True
    sedating_effects = True
    increases_depression = True
    ssris_for_depression = True
    if seroquel_for_bipolar and sedating_effects and increases_depression and not ssris_for_depression:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())