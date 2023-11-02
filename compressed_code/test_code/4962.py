def solution():
    
    candy_price = 1
    candy_weight = 12
    chips_price = 1.4
    chips_weight = 17
    max_weight = max(int((7 / candy_price)) * candy_weight, int((7 / chips_price)) * chips_weight)
    result = max_weight
    return result

print(solution())