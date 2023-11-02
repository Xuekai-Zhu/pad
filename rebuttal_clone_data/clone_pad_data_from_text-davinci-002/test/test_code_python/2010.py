def solution():
    old_model_price = 4000
    new_model_price = old_model_price * 1.3
    lens_price = 400
    lens_discount = 200
    total_price = new_model_price + lens_price - lens_discount
    result = total_price
    return result

print(solution())