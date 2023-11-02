def solution():
    gecko_sell_price = 100
    pet_store_sell_price = 3 * gecko_sell_price + 5
    pet_store_profit = pet_store_sell_price - gecko_sell_price
    result = pet_store_profit
    return result

print(solution())