def solution():
    total_fish = 36
    carla_fish = 8
    kyle_and_tasha_fish = total_fish - carla_fish
    kyle_fish = kyle_and_tasha_fish / 2
    tasha_fish = kyle_fish
    return kyle_fish, tasha_fish

print(solution())