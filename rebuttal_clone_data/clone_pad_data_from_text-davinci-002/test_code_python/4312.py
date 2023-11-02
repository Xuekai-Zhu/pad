def solution():
    lightbulbs_bedroom = 2
    lightbulbs_bathroom = 1
    lightbulbs_kitchen = 1
    lightbulbs_basement = 4
    lightbulbs_garage = lightbulbs_bathroom / 2
    total_lightbulbs = lightbulbs_bedroom + lightbulbs_bathroom + lightbulbs_kitchen + lightbulbs_basement + lightbulbs_garage
    packs_needed = total_lightbulbs / 2
    result = packs_needed
    return result

print(solution())