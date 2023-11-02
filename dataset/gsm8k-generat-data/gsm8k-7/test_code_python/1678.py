def solution():
    shampoo_price = 10.0
    conditioner_price = 10.0
    num_lotion_bottles = 3
    lotion_price = 6.0
    free_shipping_threshold = 50.0

    # Calculate the total cost of all items
    total_cost = (shampoo_price * 2) + (conditioner_price * 2) + (num_lotion_bottles * lotion_price)

    # Calculate the amount of money Jackie still needs to spend for free shipping
    amount_needed = free_shipping_threshold - total_cost
    result = amount_needed
    return result

print(solution())