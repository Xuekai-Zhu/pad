def solution():
    
    shirts_price = 12
    socks_price = 5
    shorts_price = 15
    swim_trunks_price = 14
    total_purchase_price = (3 * shirts_price) + socks_price + (2 * shorts_price) + swim_trunks_price
    if total_purchase_price < 50:
        shipping_price = 5
    else:
        shipping_price = 0.2 * total_purchase_price
    total_price = total_purchase_price + shipping_price
    result = total_price
    return result

print(solution())