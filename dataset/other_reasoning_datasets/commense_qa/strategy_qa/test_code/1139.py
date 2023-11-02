def solution():
    chris_weight = 322
    taft_weight_range = range(335, 351)
    if chris_weight in taft_weight_range:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())