def solution():
    chocolate_eggs = 12
    weight_per_egg = 10
    total_weight = chocolate_eggs * weight_per_egg
    melted_box = 1
    result = total_weight - (melted_box * weight_per_egg)
    return result

print(solution())