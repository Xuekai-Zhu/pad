def solution():
    """A porcelain vase was originally priced at $200 but went on sale for 25% off. If Donna bought the porcelain vase and paid 10% sales tax, how much did she pay in total?"""
    # Define the original price and the discount percentage
    original_price = 200
    discount_percent = 25

    # Calculate the discounted price
    discounted_price = original_price - (original_price * (discount_percent / 100))

    # Calculate the total cost with sales tax
    total_cost = discounted_price + (discounted_price * 0.1)

    # Display the total cost
    result = total_cost
    return result

print(solution())