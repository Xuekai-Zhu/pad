def solution():
    # Define the number of dress shirts and their cost
    num_shirts = 3
    shirt_cost = 20

    # Calculate the subtotal
    subtotal = num_shirts * shirt_cost

    # Calculate the tax amount
    tax_rate = 0.1
    tax_amount = subtotal * tax_rate

    # Calculate the total cost
    total_cost = subtotal + tax_amount
    result = total_cost
    return result

print(solution())