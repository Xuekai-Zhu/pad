def solution():
    monsters_seen_on_first_day = 2
    total_monsters = 0
    for day in range(5):
        monsters_seen_on_current_day = monsters_seen_on_first_day * (2 ** day)
        total_monsters += monsters_seen_on_current_day

    result = total_monsters
    return result

print(solution())