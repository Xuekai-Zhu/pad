def solution():
    polo_price = 50  # regular price of one polo shirt
    discount = 40/100  # discount percentage
    discounted_price = polo_price - (polo_price * discount)  # price after discount
    total_cost = discounted_price * 2  # total cost of two polo shirts
    result = total_cost
    return result

print(solution())