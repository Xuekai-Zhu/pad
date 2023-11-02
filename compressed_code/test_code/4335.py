def solution():
    
    books = [25, 18, 21, 35, 12, 10]
    total_price = 0
    for price in books:
        if price > 22:
            total_price += price * 0.7
        elif price < 20:
            total_price += price * 0.8
        else:
            total_price += price

    result = total_price
    return result

print(solution())