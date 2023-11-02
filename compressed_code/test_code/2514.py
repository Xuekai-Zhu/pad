def solution():
    
    grey_price = 100000
    brown_profit = 0.1
    brown_price = grey_price + (brown_profit * grey_price)
    friend_loss = 0.1
    friend_price = brown_price - (friend_loss * brown_price)
    result = friend_price
    return result

print(solution())