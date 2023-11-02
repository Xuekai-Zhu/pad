def solution():
    
    fish_per_roll = 40
    total_fish = 400
    bad_fish_percent = 20
    bad_fish = total_fish * (bad_fish_percent / 100)
    good_fish = total_fish - bad_fish
    sushi_rolls = good_fish // fish_per_roll
    result = sushi_rolls
    return result

print(solution())