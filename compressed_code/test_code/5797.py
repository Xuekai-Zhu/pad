def solution():
    
    shorts_price = 7
    num_shorts = 5
    shoes_price = 10
    num_shoes = 2
    total_spent = 75
    total_spent -= (shorts_price*num_shorts + shoes_price*num_shoes)
    num_tops = 4
    top_price = total_spent / num_tops
    result = top_price
    return result

print(solution())