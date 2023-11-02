def solution():
    
    shorts_price = 7
    shoes_price = 10
    tops_total_price = 75 - (5 * shorts_price) - (2 * shoes_price)
    tops_each_price = tops_total_price / 4
    result = tops_each_price
    return result

print(solution())