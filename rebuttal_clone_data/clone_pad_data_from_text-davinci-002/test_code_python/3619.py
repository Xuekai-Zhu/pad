def solution():
    coffee = 6
    cheesecake = 10
    discount = 0.25
    total_price = coffee + cheesecake
    discounted_price = total_price - (total_price * discount)
    result = discounted_price
    return result

print(solution())