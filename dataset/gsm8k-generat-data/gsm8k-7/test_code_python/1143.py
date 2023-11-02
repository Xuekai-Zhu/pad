def solution():
    wooden_toy_price = 20
    hat_price = 10
    num_wooden_toys = 2
    num_hats = 3
    total_cost = (wooden_toy_price * num_wooden_toys) + (hat_price * num_hats)
    amount_paid = 100
    change = amount_paid - total_cost
    result = change
    return result

print(solution())