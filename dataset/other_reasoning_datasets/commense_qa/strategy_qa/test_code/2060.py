def solution():
    newt_skin = "smooth and sticky"
    reptile_skin = "dry and hard"
    if newt_skin in "Newt" and newt_skin != reptile_skin:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())