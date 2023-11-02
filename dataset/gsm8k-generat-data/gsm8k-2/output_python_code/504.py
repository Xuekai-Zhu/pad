def solution():
    """Carla's sheepdog rounded up 90% of her sheep, but the remaining 10% wandered off into the hills. If there are 81 sheep in the pen, how many are out in the wilderness?"""
    total_sheep = 100
    sheepdog_sheep = 90
    remaining_sheep = 10
    sheep_in_pen = 81
    sheep_in_wilderness = (remaining_sheep / total_sheep) * sheep_in_pen
    result = sheep_in_wilderness
    return result

print(solution())