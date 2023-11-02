def solution():
    # Calculate the discounted price of each chair
    discounted_price = 0.75 * 20  # 25% off $20 is $15

    # Calculate the total cost of the first 5 chairs
    first_five_chairs_cost = 5 * discounted_price

    # Calculate the total cost of the remaining 3 chairs after the additional discount
    remaining_chairs_cost = 3 * (2/3 * discounted_price)

    # Calculate the total cost of all 8 chairs
    total_cost = first_five_chairs_cost + remaining_chairs_cost
    result = total_cost
    return result

print(solution())