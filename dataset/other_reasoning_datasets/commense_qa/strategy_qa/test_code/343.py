def solution():
    frost_forms = True
    snow_falls = False
    if frost_forms and not snow_falls:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())