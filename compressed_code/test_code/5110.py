def solution():
    
    old_price = 85
    new_price = 102
    increase = new_price - old_price
    percent_increase = (increase / old_price) * 100
    result = percent_increase
    return result

print(solution())