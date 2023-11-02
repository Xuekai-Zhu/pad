def solution():
    wow_weight = 0
    bread_weight = 0.5     # assuming the weight of the bread is 500g
    if wow_weight > bread_weight:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())