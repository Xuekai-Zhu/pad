def solution():
    part_price = 80  # price of one part
    num_parts = 7   # number of parts bought
    total_price = 439  # total price paid

    # calculate discounted price per part
    discounted_price = total_price / num_parts 

    # calculate discount per part
    discount = part_price - discounted_price

    result = discount
    return result

print(solution())