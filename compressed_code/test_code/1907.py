def solution():
    
    num_shirts = 10
    shirt_price = 5
    num_sandals = 3
    sandal_price = 3
    total_cost = (num_shirts * shirt_price) + (num_sandals * sandal_price)
    paid_amount = 100
    change = paid_amount - total_cost
    result = change
    return result

print(solution())