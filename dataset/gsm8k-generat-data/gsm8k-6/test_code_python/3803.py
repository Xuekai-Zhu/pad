def solution():
    # Calculate the total cost of the t-shirts before the discount
    cost_before_discount = 5 * 4 * 15  # 5 t-shirts from each of the 4 fandoms, at $15 each

    # Calculate the amount of the discount
    discount = 0.2 * cost_before_discount

    # Calculate the total cost of the t-shirts after the discount
    cost_after_discount = cost_before_discount - discount

    # Calculate the amount of tax
    tax = 0.1 * cost_after_discount

    # Calculate the total cost including tax and the discount
    total_cost = cost_after_discount + tax

    result = total_cost
    return result

print(solution())