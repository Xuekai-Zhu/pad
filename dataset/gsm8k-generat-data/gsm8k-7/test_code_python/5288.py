def solution():
    num_backpacks = 5
    regular_price = 20.0
    discount = 0.2  # 20% off
    monogram_price = 12.0

    # Calculate the discounted price of each backpack
    discounted_price = regular_price * (1 - discount)

    # Calculate the total cost of all backpacks before monogramming
    total_cost_before_monogram = num_backpacks * discounted_price

    # Calculate the total cost of monogramming all backpacks
    total_monogram_cost = num_backpacks * monogram_price

    # Calculate the total cost of all backpacks with monogramming
    total_cost = total_cost_before_monogram + total_monogram_cost
    result = total_cost
    return result

print(solution())