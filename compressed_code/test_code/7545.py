def solution():
    
    tv_price = 650
    num_tv = 2
    percent_discount = 25
    discount_amount = (tv_price * percent_discount) / 100
    discounted_price = tv_price - discount_amount
    total_price = discounted_price * num_tv
    result = total_price
    return result

print(solution())