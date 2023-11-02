def solution():
    num_shirts = 10
    shirt_price = 5

    num_sandals = 3
    sandals_price = 3

    total_cost = (num_shirts * shirt_price) + (num_sandals * sandals_price)
    change = 100 - total_cost
    result = change
    return result

print(solution())