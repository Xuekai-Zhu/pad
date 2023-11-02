def solution():
    fries_price = 2  # One pack of fries costs $2
    salad_price = 3 * fries_price  # The salad costs 3 times the price of one pack of fries
    total_price = 15  # Benjamin paid $15 in total
    burger_price = (total_price - (salad_price + 2 * fries_price)) / 1  # Subtract the price of salad and fries, and divide by 1 (for the burger)

    result = burger_price
    return result

print(solution())