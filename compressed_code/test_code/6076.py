def solution():
    
    shoes_discount = 40
    dress_discount = 20
    shoes_price = 50
    dress_price = 100
    discounted_shoes_price = shoes_price * (100 - shoes_discount) / 100
    discounted_dress_price = dress_price * (100 - dress_discount) / 100
    total_price = (discounted_shoes_price * 2) + discounted_dress_price
    result = total_price
    return result

print(solution())