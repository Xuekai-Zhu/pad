def solution():
    white_price = 5
    swiss_price = 6
    blue_price = 8
    white_grams = 200
    swiss_grams = 200
    blue_grams = 200
    white_amount = (5 * swiss_grams) - (white_grams / 3)
    swiss_amount = 5 * swiss_grams
    blue_amount = 600 * blue_grams
    total_cost = (white_price * white_amount) + (swiss_price * swiss_amount) + (blue_price * blue_amount)
    result = total_cost
    return result

print(solution())