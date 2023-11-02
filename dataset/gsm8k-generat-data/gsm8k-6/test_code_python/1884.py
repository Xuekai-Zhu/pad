def solution():
    sandbag_weight = 250  # pounds
    filling_material_weight = 1.4 * sandbag_weight * 0.8  # 40% heavier than sand, filled 80% full
    total_weight = sandbag_weight + filling_material_weight
    result = total_weight
    return result

print(solution())