def solution():
    
    suit_price = 700
    shirt_price = 50
    loafers_price = 150
    total_suit_price = 2 * suit_price
    total_shirt_price = 6 * shirt_price
    total_loafers_price = 2 * loafers_price
    total_sales_price = total_suit_price + total_shirt_price + total_loafers_price
    commission_rate = 0.15
    commission_amount = commission_rate * total_sales_price
    result = commission_amount
    return result

print(solution())