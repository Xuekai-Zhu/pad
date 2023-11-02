def solution():
    # Calculate how much John used to spend per day
    old_price = 2
    old_quantity = 4
    old_cost = old_price * old_quantity

    # Calculate the new price and quantity after the price increase and quantity change
    new_price = old_price * 1.5
    new_quantity = old_quantity / 2

    # Calculate how much John spends now
    new_cost = new_price * new_quantity

    # Calculate the difference between the old and new costs
    difference = old_cost - new_cost
    result = difference
    return result

print(solution())