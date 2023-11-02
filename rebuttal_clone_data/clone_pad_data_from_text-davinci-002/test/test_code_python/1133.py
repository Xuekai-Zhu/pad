def solution():
    fish_per_heated_tank = 15
    fish_per_unheated_tank = 10
    total_fish = 75
    heated_tanks = 3
    unheated_tanks = total_fish - (heated_tanks * fish_per_heated_tank)
    result = unheated_tanks / fish_per_unheated_tank
    return result

print(solution())