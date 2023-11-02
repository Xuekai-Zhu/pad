def solution():
    cost = 15000
    percent_off = 40
    original_price = cost / (1 - (percent_off/100))
    result = original_price
    
    return result

print(solution())