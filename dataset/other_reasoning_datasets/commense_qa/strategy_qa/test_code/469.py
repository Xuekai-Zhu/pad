def solution():
    under_renovation = True
    bells_silenced = True
    normal_schedule = False
    if not under_renovation and not bells_silenced and normal_schedule:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())