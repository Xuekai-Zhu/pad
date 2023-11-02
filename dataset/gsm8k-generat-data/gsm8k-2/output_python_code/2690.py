def solution():
    """Carla, Kyle, and Tasha caught 36 fish. If Kyle and Tasha caught the same number of fish and Carla caught 8, how many fish did Kyle catch?"""
    total_fish = 36
    carla_fish = 8
    remaining_fish = total_fish - carla_fish
    kyle_tasha_fish = remaining_fish / 2
    result = kyle_tasha_fish
    return result

print(solution())