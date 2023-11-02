def solution():
    shirts_per_fandom = 5  # Tom buys 5 t-shirts from each of his 4 favorite fandoms
    num_fandoms = 4  # Tom has 4 favorite fandoms

    # Calculate the total cost of the shirts before discount
    cost_before_discount = shirts_per_fandom * num_fandoms * 15

    # Calculate the discount amount
    discount_percent = 20
    discount_amount = cost_before_discount * (discount_percent / 100)

    # Calculate the cost after discount
    cost_after_discount = cost_before_discount - discount_amount

    # Calculate the tax amount
    tax_percent = 10
    tax_amount = cost_after_discount * (tax_percent / 100)

    # Calculate the total cost including tax
    total_cost = cost_after_discount + tax_amount
    result = total_cost
    return result

print(solution())