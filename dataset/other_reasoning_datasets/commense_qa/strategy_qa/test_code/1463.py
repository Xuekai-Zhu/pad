def solution():
    commodus_reign_start = 180
    commodus_reign_end = 192
    pound_sterling_origin = 5th century AD
    if commodus_reign_start <= pound_sterling_origin <= commodus_reign_end:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())