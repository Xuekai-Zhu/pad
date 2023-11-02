def solution():
    
    first_day_monsters = 2
    total_monsters = 0
    for i in range(5):
        daily_monsters = first_day_monsters * (2 ** i)
        total_monsters += daily_monsters
    result = total_monsters
    return result

print(solution())