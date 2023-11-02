def solution():
    shirts_on_sale = 6  # Marlene wants to buy half a dozen shirts
    regular_price = 50  # The regular price of a shirt is $50
    discount = 0.2  # The shirts are on sale with a 20% discount

    # Calculate the discounted price of a shirt
    discounted_price = regular_price * (1 - discount)

    # Calculate the total cost of the shirts on sale
    total_cost = shirts_on_sale * discounted_price
    result = total_cost
    return result

print(solution())