def solution():
    lunch_cost = 100  # The cost of Greg's lunch is $100
    sales_tax_percent = 4  # Sales tax in New York is 4%
    tip_percent = 6  # Greg left a 6% tip

    # Calculate the sales tax amount
    sales_tax_amount = lunch_cost * (sales_tax_percent / 100)

    # Calculate the tip amount
    tip_amount = lunch_cost * (tip_percent / 100)

    # Calculate the total amount paid by Greg
    total_cost = lunch_cost + sales_tax_amount + tip_amount
    result = total_cost
    return result

print(solution())