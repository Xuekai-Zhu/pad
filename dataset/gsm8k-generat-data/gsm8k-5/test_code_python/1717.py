def solution():
    # Calculate the total cost of 3 pairs of jeans without discount
    total_cost = 3 * 40  # Each pair of jeans costs $40

    # Apply the 10% discount for every 2 pairs of jeans
    pairs_with_discount = 3 // 2  # Round down to the nearest whole number
    discount = pairs_with_discount * 0.1 * 2 * 40  # 10% discount for every 2 pairs of jeans
    final_cost = total_cost - discount

    result = final_cost
    return result

print(solution())