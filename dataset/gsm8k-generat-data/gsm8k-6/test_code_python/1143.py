def solution():
    wooden_toy_price = 20
    hat_price = 10
    bill_amount = 100

    # Calculate the total cost of two wooden toys and three hats
    total_cost = (2 * wooden_toy_price) + (3 * hat_price)

    # Calculate the change Kendra received
    change = bill_amount - total_cost
    result = change
    return result

print(solution())