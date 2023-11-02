def solution():
    dish_prices = [10, 13, 17]  # Prices of the dishes
    total_bill = sum(dish_prices)  # Total cost of the dishes
    tip_percent = 10  # 10% tip
    tip_amount = (tip_percent / 100) * total_bill  # Calculating tip amount
    result = tip_amount
    return result

print(solution())