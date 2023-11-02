def solution():
    shot_weight = 16.01
    fox_weight_range = range(5, 10)
    if shot_weight > max(fox_weight_range):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())