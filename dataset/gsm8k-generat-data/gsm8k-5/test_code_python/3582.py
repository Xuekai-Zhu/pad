def solution():
    current_model_cost = 4000
    new_model_cost = current_model_cost * 1.3  # 30% more than the current model
    lens_discount = 200
    lens_cost = 400
    total_cost = new_model_cost + lens_cost - lens_discount
    result = total_cost
    return result

print(solution())