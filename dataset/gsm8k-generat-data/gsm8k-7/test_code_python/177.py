def solution():
    initial_car_value = 20000
    selling_price = 0.8 * initial_car_value

    new_car_sticker_price = 30000
    buying_price = 0.9 * new_car_sticker_price

    out_of_pocket = buying_price - selling_price
    result = out_of_pocket
    return result

print(solution())