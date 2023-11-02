def solution():
    num_fandoms = 4
    num_tshirts = 5
    tshirt_price = 15
    discount = 0.2
    tax = 0.1

    # Calculate the total cost of all t-shirts before discounts and taxes
    total_cost = num_fandoms * num_tshirts * tshirt_price

    # Calculate the discount on the total cost
    discount_amount = total_cost * discount

    # Calculate the cost after the discount
    cost_after_discount = total_cost - discount_amount

    # Calculate the tax on the cost after the discount
    total_cost_with_tax = cost_after_discount * (1 + tax)

    result = total_cost_with_tax
    return result

print(solution())