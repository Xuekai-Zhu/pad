def solution():
    original_price = 100000
    first_sale_profit = 100000 * 0.1
    first_sale_price = 100000 + first_sale_profit
    second_sale_loss = first_sale_price * 0.1
    second_sale_price = first_sale_price - second_sale_loss
    result = second_sale_price
    return result

print(solution())