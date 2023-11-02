def solution():
    broken_bulbs_kitchen = 3/5
    broken_bulbs_foyer = 1/3
    light_bulbs_kitchen = 35
    light_bulbs_foyer = 10
    total_bulbs_kitchen = light_bulbs_kitchen * broken_bulbs_kitchen
    total_bulbs_foyer = light_bulbs_foyer * broken_bulbs_foyer
    light_bulbs_not_broken = light_bulbs_foyer - total_bulbs_foyer + light_bulbs_kitchen - total_bulbs_kitchen
    result = light_bulbs_not_broken
    return result

print(solution())