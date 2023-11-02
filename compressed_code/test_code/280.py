def solution():
    
    shoe_price = 50
    dress_price = 100
    shoe_discount = 0.4
    dress_discount = 0.2
    total_shoe_price = 2 * shoe_price * (1 - shoe_discount)
    total_dress_price = dress_price * (1 - dress_discount)
    total_price = total_shoe_price + total_dress_price
    result = total_price
    return result

print(solution())