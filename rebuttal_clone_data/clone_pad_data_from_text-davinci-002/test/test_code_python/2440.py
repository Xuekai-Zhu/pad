def solution():
    fish_caught_jordan = 4
    fish_caught_perry = fish_caught_jordan * 2
    total_fish_caught = fish_caught_jordan + fish_caught_perry
    fish_lost = total_fish_caught / 4
    fish_remaining = total_fish_caught - fish_lost
    result = fish_remaining
    
    return result

print(solution())