def solution():
    num_monsters_day_one = 2
    total_monsters = num_monsters_day_one
    for day in range(2, 6):
        num_monsters_today = num_monsters_day_one * (2 ** (day - 1))
        total_monsters += num_monsters_today
    result = total_monsters
    return result

print(solution())