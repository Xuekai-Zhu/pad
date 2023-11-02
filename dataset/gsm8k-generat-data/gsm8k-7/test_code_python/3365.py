def solution():
    num_shirts = 3
    shirt_price = 20
    tax_rate = 0.1  # 10% tax rate

    # Calculate the total cost of all dress shirts
    total_shirt_cost = num_shirts * shirt_price

    # Calculate the tax amount on the total cost
    tax_amount = total_shirt_cost * tax_rate

    # Calculate the total cost including tax
    total_cost_with_tax = total_shirt_cost + tax_amount
    result = total_cost_with_tax
    return result

print(solution())