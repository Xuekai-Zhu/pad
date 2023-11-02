def solution():
    backpack_price = 20  # Original price of the backpack
    discount_percent = 20  # Backpacks are 20% off
    num_backpacks = 5  # Grandma is ordering 5 backpacks
    monogram_cost = 12  # Cost of adding a monogram to each backpack

    # Calculate the discounted price of each backpack
    discounted_price = backpack_price - (backpack_price * discount_percent / 100)

    # Calculate the total cost of the backpacks
    backpack_cost = (discounted_price + monogram_cost) * num_backpacks
    result = backpack_cost
    return result

print(solution())