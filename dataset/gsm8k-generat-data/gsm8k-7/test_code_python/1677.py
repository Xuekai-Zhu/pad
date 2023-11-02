def solution():
    min_purchase = 18

    num_burgers = 2
    burger_price = 3.2

    num_fries = 2
    fries_price = 1.9

    num_milkshakes = 2
    milkshake_price = 2.4

    # Calculate the total cost of Danny's order
    total_cost = (num_burgers * burger_price) + (num_fries * fries_price) + (num_milkshakes * milkshake_price)

    # Calculate how much more Danny needs to spend to reach the minimum purchase for free delivery
    remaining_cost = min_purchase - total_cost
    result = remaining_cost
    return result

print(solution())