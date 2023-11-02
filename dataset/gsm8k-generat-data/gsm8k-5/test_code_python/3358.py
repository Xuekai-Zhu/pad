def solution():
    num_nose_sprays = 10  # Bob buys 10 nose sprays
    cost_per_spray = 3  # Each spray costs $3
    num_sprays_to_pay_for = num_nose_sprays / 2  # With the promotion, Bob gets one free spray for each one purchased
    total_cost = num_sprays_to_pay_for * cost_per_spray  # Bob pays for half of the sprays
    result = total_cost
    return result

print(solution())