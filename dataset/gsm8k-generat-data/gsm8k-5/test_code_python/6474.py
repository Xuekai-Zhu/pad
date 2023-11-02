def solution():
    # Calculate the total revenue for company A
    price_a = 4  # The price of a big bottle of milk for company A
    quantity_a = 300  # The number of big bottles of milk sold by company A
    revenue_a = price_a * quantity_a

    # Calculate the total revenue for company B
    price_b = 3.5  # The price of a big bottle of milk for company B
    quantity_b = 350  # The number of big bottles of milk sold by company B
    revenue_b = price_b * quantity_b

    # Calculate the difference in revenue between the two companies
    difference = abs(revenue_a - revenue_b)
    result = difference
    return result

print(solution())