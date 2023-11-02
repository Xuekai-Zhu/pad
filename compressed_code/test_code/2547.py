def solution():
    
    starting_fish = 60
    bobbit_worm_days = 21
    bobbit_worm_fish_eaten = bobbit_worm_days * 2
    james_added_fish = 8
    total_fish = starting_fish + james_added_fish - bobbit_worm_fish_eaten
    result = total_fish
    return result

print(solution())