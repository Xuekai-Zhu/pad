def solution():
    monthly_price = 10
    discount = 0.2 # 20% discount
    num_months = 12

    # Calculate the total cost without the discount
    total_cost = monthly_price * num_months

    # Calculate the discounted price
    discounted_price = total_cost * (1 - discount)

    result = discounted_price
    return result

print(solution())