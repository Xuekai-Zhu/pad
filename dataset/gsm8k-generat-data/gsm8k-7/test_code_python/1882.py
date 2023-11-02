def solution():
    bananas_left = 100
    bananas_eaten = 70
    remaining_basket = bananas_left - bananas_eaten
    initial_bananas = remaining_basket * 2
    total_bananas = initial_bananas + bananas_eaten
    result = total_bananas
    return result

print(solution())