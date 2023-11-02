def solution():
    has_down_syndrome = True
    disqualified_from_military = True
    if not has_down_syndrome and not disqualified_from_military:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())