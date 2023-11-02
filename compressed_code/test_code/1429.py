def solution():
    
    total_nickels = 95 // 5
    ray_gives_peter = 25
    ray_gives_randi = 2*ray_gives_peter
    total_given_away = ray_gives_peter + ray_gives_randi
    nickels_left = total_nickels - (total_given_away // 5)
    result = nickels_left
    return result

print(solution())