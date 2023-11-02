def solution():
    total_cost = 240000  # Princess Daphne spent a total of $240,000
    num_necklaces = 3  # Princess Daphne bought three necklaces
    cost_earrings = 3 * cost_necklace  # The earrings cost three times as much as any one necklace

    # Calculate the total cost of the necklaces
    total_cost_necklaces = total_cost - cost_earrings
    cost_single_necklace = total_cost_necklaces / num_necklaces
    result = cost_single_necklace
    return result

print(solution())