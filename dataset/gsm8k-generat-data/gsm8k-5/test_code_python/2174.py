def solution():
    original_price = 120  # Original price of the aquarium
    discount = 0.5  # The aquarium is marked down by 50%
    reduced_price = original_price * (1 - discount)  # Calculating the reduced price
    sales_tax_rate = 0.05  # Sales tax rate is 5%

    # Calculating the sales tax amount
    sales_tax = reduced_price * sales_tax_rate

    # Calculating the total cost of the aquarium, including sales tax
    total_cost = reduced_price + sales_tax
    result = total_cost
    return result

print(solution())