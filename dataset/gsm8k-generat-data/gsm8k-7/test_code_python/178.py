def solution():
    discount = 0.1  # 10% discount
    pansies_quantity = 5
    pansies_price = 2.5
    hydrangea_price = 12.5
    petunias_quantity = 5
    petunias_price = 1.0
    total_price = (pansies_quantity * pansies_price) + hydrangea_price + (petunias_quantity * petunias_price)
    discounted_price = total_price * (1 - discount)
    change = 50 - discounted_price
    result = change
    return result

print(solution())