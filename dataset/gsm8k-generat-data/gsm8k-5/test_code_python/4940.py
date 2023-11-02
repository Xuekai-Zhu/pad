def solution():
    # Calculate the total number of pens bought at regular price and half off
    total_pens = 20
    pens_at_regular_price = 10
    pens_at_half_price = 10

    # Calculate the total cost of the pens
    total_cost = 30

    # Calculate the cost of the pens bought at regular price
    cost_at_regular_price = pens_at_regular_price * x

    # Calculate the cost of the pens bought at half price
    cost_at_half_price = (pens_at_half_price * x) / 2

    # Calculate the regular price of one pen
    regular_price = (cost_at_regular_price + cost_at_half_price) / total_pens
    result = regular_price
    return result

print(solution())