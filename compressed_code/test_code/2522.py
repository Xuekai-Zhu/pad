def solution():
    
    needed_fish_per_roll = 40
    total_fish = 400
    bad_fish_percentage = 0.2
    good_fish = (1 - bad_fish_percentage) * total_fish
    sushi_rolls = good_fish // needed_fish_per_roll
    result = sushi_rolls
    return result

print(solution())