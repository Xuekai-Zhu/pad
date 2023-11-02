def solution():
    """A porcelain vase was originally priced at $200 but went on sale for 25% off. If Donna bought the porcelain vase and paid 10% sales tax, how much did she pay in total?"""
    # Define the original price of the porcelain vase
    original_price = 200

    # Calculate the sale price of the porcelain vase, after a 25% discount
    sale_price = original_price * (1 - 0.25)

    # Calculate the total price, including 10% sales tax
    total_price = sale_price * 1.1

    # Round the total price to two decimal places
    total_price = round(total_price, 2)

    # Return the total price
    result = total_price
    return result

print(solution())