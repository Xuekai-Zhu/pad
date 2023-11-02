def solution():
    num_pants = 2
    pants_price = 54

    num_shirts = 4
    shirt_price = 33

    total_cost = (num_pants * pants_price) + (num_shirts * shirt_price)
    cash_given = 250

    change = cash_given - total_cost
    result = change
    return result

print(solution())