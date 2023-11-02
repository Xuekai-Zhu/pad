def solution():
    
    lawn_price = 6
    weed_price = 11
    mulch_price = 9
    lawn_hours = 63
    weed_hours = 9
    mulch_hours = 10
    total_money = (lawn_price * lawn_hours) + (weed_price * weed_hours) + (mulch_price * mulch_hours)
    result = total_money
    return result

print(solution())