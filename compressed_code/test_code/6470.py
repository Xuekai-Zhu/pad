def solution():
    
    initial_coins = 80
    donated_coins = 20
    remaining_coins = initial_coins - donated_coins
    half_coins = remaining_coins / 2
    tripled_coins = half_coins * 3
    final_coins = tripled_coins - 10
    result = final_coins
    return result

print(solution())