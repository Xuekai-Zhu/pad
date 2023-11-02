def solution():
    # Calculate the total cost of the flowers before the discount
    pansies_cost = 5 * 2.5  # 5 pansies at $2.50 each
    hydrangea_cost = 12.5  # 1 hydrangea that costs $12.50
    petunias_cost = 5 * 1  # 5 petunias at $1.00 each
    total_cost = pansies_cost + hydrangea_cost + petunias_cost

    # Apply the 10% discount
    discount = 0.1 * total_cost
    discounted_price = total_cost - discount

    # Calculate Simon's change
    change = 50 - discounted_price
    result = change
    return result

print(solution())