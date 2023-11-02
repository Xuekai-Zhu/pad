def solution():
    
    adidas_purchase = 600
    nike_purchase = adidas_purchase * 3
    skechers_purchase = adidas_purchase * 5
    total_sneaker_purchase = adidas_purchase + nike_purchase + skechers_purchase
    clothes_purchase = 8000 - total_sneaker_purchase
    result = clothes_purchase
    return result

print(solution())