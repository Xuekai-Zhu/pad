def solution():
    copper_weight = 90
    steel_weight = copper_weight + 20
    tin_weight = steel_weight / 2
    total_weight = steel_weight + copper_weight + (tin_weight * 20)
    result = total_weight
    return result

print(solution())