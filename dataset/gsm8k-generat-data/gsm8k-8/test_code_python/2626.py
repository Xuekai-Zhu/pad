def solution():
    initial_cost = 50.00
    discount = 0.10
    embroidery_cost = 5.50 * 2
    shipping_cost = 10.00

    # Calculate the discounted cost
    discounted_cost = initial_cost * (1 - discount)

    # Calculate the total cost
    total_cost = discounted_cost + embroidery_cost + shipping_cost
    result = total_cost
    return result

print(solution())