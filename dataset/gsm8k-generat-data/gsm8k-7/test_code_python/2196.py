def solution():
    cost = 200
    tax = 0.15  # 15% tax

    # Calculate the amount of tax John pays
    tax_amount = cost * tax

    # Add the tax amount to the original cost to get the total amount John paid
    total_paid = cost + tax_amount

    result = total_paid
    return result

print(solution())