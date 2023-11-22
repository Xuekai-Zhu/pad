def solution():
    
    phone_price = 600
    num_phones = 4
    total_cost = phone_price * num_phones
    for i in range(1, num_phones + 1):
        cost_after_i = phone_price / 2
        total_cost += cost_after_i
    result = total_cost
    return result

print(solution())