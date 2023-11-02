def solution():
    copper_weight = 90
    steel_weight = copper_weight + 20
    tin_weight = steel_weight / 2
    total_weight = (20 * copper_weight) + (20 * steel_weight) + (20 * tin_weight)
    result = total_weight
    return result

print(solution())