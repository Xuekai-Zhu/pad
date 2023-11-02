def solution():
    fish = 6
    fish_doubled = fish * 2
    fish_removed = fish_doubled / 3
    fish_removed_2 = fish_doubled - fish_removed
    fish_removed_3 = fish_removed_2 / 4
    fish_removed_4 = fish_removed_2 - fish_removed_3
    fish_added = fish_removed_4 + 15
    fish_total = fish_added + fish_removed_3 + fish_removed
    result = fish_total
    
    return result

print(solution())