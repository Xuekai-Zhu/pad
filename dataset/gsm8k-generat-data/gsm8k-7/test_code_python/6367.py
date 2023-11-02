def solution():
    product_cost = 90
    markup = 10
    tax_percent = 10

    # Calculate the selling price of the product with the markup
    selling_price = product_cost + markup

    # Calculate the tax to be paid on the sale
    tax = selling_price * (tax_percent / 100)

    # Calculate Bert's profit on the sale
    profit = selling_price - product_cost - tax
    result = profit
    return result

print(solution())