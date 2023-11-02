def solution():
    
    initial_coins = 20
    additional_coins = 30*2 + 40
    coins_borrowed = 20
    total_coins = initial_coins + additional_coins - coins_borrowed
    result = total_coins
    return result

print(solution())