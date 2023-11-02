def solution():
    apple_price = 1
    orange_price = 2
    banana_price = 3
    discount_rate = 1
    apples = 5
    oranges = 3
    bananas = 2
    total_price = (apples * apple_price) + (oranges * orange_price) + (bananas * banana_price)
    discount_amount = total_price / 5
    total_discount = discount_rate * discount_amount
    final_price = total_price - total_discount
    result = final_price
    return result

print(solution())