def solution():
    total_sheep = 81
    sheepdog_rounded = 0.9 * total_sheep  # 90% of the sheep were rounded up
    wandering_sheep = total_sheep - sheepdog_rounded  # the rest of the sheep wandered off

    result = wandering_sheep
    return result

print(solution())