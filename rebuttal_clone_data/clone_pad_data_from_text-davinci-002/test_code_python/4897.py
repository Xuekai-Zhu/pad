def solution():
    total_fish = 80
    blue_fish = total_fish / 2
    orange_fish = blue_fish - 15
    green_fish = total_fish - (blue_fish + orange_fish)
    result = green_fish
    
    return result

print(solution())