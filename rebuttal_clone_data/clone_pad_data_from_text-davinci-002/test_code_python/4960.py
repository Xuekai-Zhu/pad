def solution():
    dish_price_1 = 10
    dish_price_2 = 13
    dish_price_3 = 17
    percentage_tip = 10
    total_bill = dish_price_1 + dish_price_2 + dish_price_3
    gratuity = total_bill * (percentage_tip / 100)
    result = gratuity
    return result

print(solution())