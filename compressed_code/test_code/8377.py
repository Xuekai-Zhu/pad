def solution():
    
    initial_fish = 60
    days_before_discovery = 21
    fish_eaten = days_before_discovery * 2
    fish_after_two_weeks = initial_fish - fish_eaten
    fish_after_addition = fish_after_two_weeks + 8
    result = fish_after_addition
    return result

print(solution())