def solution():
    scottish_origin = ["Picts", "Gaels"]
    picts_self_reference = "Albidosi"
    if picts_self_reference in scottish_origin:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())