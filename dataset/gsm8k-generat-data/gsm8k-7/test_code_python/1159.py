def solution():
    shoes_price = 200
    shoes_discount = 0.3
    shirts_price = 80
    num_shirts = 2
    additional_discount = 0.05

    # Calculate the discounted price of the shoes
    discounted_shoes_price = shoes_price * (1 - shoes_discount)

    # Calculate the total cost of the shirts
    total_shirts_cost = shirts_price * num_shirts

    # Calculate the subtotal before the additional discount
    subtotal = discounted_shoes_price + total_shirts_cost

    # Calculate the additional discount amount
    additional_discount_amount = subtotal * additional_discount

    # Calculate the total cost after all discounts
    total_cost = subtotal - additional_discount_amount
    result = total_cost
    return result

print(solution())