def solution():
    current_model_cost = 4000
    new_model_cost = current_model_cost * 1.3
    lens_cost = 400
    discount = 0.5
    discounted_lens_cost = lens_cost * (1 - discount)
    total_cost = new_model_cost + discounted_lens_cost
    result = total_cost
    return result

print(solution())