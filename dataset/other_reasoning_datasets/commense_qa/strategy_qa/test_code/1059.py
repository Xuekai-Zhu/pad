def solution():
    religion = "Judaism"
    holiday = "Christmas"
    if religion != "Christianity" and holiday == "Christmas":
        result = "no"
    else:
        result = "yes"
    return result

print(solution())