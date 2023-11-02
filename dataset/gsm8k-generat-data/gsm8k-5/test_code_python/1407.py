def solution():
    first_pair_price = 22  # Nina bought the first pair for $22
    second_pair_price = 1.5 * first_pair_price  # The second pair was 50% more expensive

    # Calculate the total cost of both pairs of shoes
    total_cost = 2 * (first_pair_price + second_pair_price)
    result = total_cost
    return result

print(solution())