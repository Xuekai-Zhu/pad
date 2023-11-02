def solution():
    # Define the number of pens and the total cost
    total_pens = 20
    total_cost = 30

    # Calculate the number of pens at regular price and half off price
    pens_regular_price = 10
    pens_half_off_price = total_pens - pens_regular_price

    # Calculate the cost of pens at regular price and half off price
    cost_regular_price = total_cost * (pens_regular_price / total_pens)
    cost_half_off_price = total_cost * (pens_half_off_price / total_pens) * 2

    # Calculate the total cost of all pens at regular price and half off price
    total_cost_regular_price = pens_regular_price * cost_regular_price
    total_cost_half_off_price = pens_half_off_price * cost_half_off_price

    # Calculate the regular price of one pen
    regular_price = total_cost_regular_price / pens_regular_price
    result = regular_price
    return result

print(solution())