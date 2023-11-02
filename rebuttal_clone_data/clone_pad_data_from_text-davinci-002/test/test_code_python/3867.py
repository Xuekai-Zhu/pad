def solution():
    ben_fish = 4
    judy_fish = 1
    billy_fish = 3
    jim_fish = 2
    susie_fish = 5
    fish_caught = ben_fish + judy_fish + billy_fish + jim_fish + susie_fish
    fish_thrown_back = 3
    fish_kept = fish_caught - fish_thrown_back
    filets_per_fish = 2
    total_filets = fish_kept * filets_per_fish
    result = total_filets
    return result

print(solution())