def solution():
    total_amount = 150  # The total amount of all the items Pauline wants to buy is $150
    sales_tax = 0.08  # The sales tax is 8% of the total amount purchased

    # Calculate the sales tax amount
    tax_amount = total_amount * sales_tax

    # Calculate the total amount with sales tax
    total_with_tax = total_amount + tax_amount
    result = total_with_tax
    return result

print(solution())