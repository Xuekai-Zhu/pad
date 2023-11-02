def solution():
    cakes = 6
    minutes_to_mix = 12
    minutes_to_bake = minutes_to_mix + 9
    minutes_to_cool = minutes_to_bake + 6
    total_minutes = (minutes_to_mix * cakes) + (minutes_to_bake * cakes) + (minutes_to_cool * cakes)
    hours = total_minutes / 60
    result = hours
    return result

print(solution())