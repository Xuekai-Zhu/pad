def solution():
    jacques_duzeze_religion = "Christianity"
    richard_dawkins_beliefs = "critic of religion"
    if jacques_duzeze_religion != "" and richard_dawkins_beliefs != "pro-religion":
        result = "no"
    else:
        result = "unclear"
    return result

print(solution())