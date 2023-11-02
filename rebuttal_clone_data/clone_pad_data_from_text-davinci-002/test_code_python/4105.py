def solution():
    donuts_eaten_monday = 14
    donuts_eaten_tuesday = donuts_eaten_monday / 2
    donuts_eaten_wednesday = donuts_eaten_monday * 4
    total_donuts = donuts_eaten_monday + donuts_eaten_tuesday + donuts_eaten_wednesday
    result = total_donuts
    return result

print(solution())