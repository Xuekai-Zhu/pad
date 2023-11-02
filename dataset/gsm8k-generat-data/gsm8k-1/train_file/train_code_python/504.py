def solution():
    """Carla's sheepdog rounded up 90% of her sheep, but the remaining 10% wandered off into the hills. If there are 81 sheep in the pen, how many are out in the wilderness?"""
    total_sheep = 81
    percent_rounded_up = 90
    percent_wandered_off = 10
    sheep_rounded_up = total_sheep * (percent_rounded_up / 100)
    sheep_wandered_off = total_sheep - sheep_rounded_up
    result = sheep_wandered_off
    
    return result

print(solution())