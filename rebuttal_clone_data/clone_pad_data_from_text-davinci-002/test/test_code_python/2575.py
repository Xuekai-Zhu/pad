def solution():
    cows = 40
    water_per_cow = 80
    sheep = cows * 10
    water_per_sheep = water_per_cow * (1/4)
    total_water = (water_per_cow * cows) + (water_per_sheep * sheep)
    water_per_week = total_water * 7
    result = water_per_week
    return result

print(solution())