def solution():
    total_volume = 150
    oil_volume = total_volume * (2/3)
    vinegar_volume = total_volume * (1/3)
    oil_weight = oil_volume * 5
    vinegar_weight = vinegar_volume * 4
    total_weight = oil_weight + vinegar_weight
    result = total_weight
    return result

print(solution())