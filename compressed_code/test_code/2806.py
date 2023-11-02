def solution():
    
    coffee_price = 6
    cheesecake_price = 10
    discount = 0.25
    total_price = coffee_price + cheesecake_price
    discounted_price = total_price - (total_price * discount)
    result = discounted_price
    return result

print(solution())