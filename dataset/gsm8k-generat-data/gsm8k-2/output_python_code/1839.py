def solution():
    """Ray has 95 cents in nickels. If Ray gives 25 cents to Peter, and twice as many cents to Randi as he gave to Peter, how many nickels does Ray have left?"""
    total_nickels = 95 // 5
    ray_gives_peter = 25
    ray_gives_randi = 2*ray_gives_peter
    total_given_away = ray_gives_peter + ray_gives_randi
    nickels_left = total_nickels - (total_given_away // 5)
    result = nickels_left
    return result

print(solution())