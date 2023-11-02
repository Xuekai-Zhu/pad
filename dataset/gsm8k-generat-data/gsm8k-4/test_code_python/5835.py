def solution():
    """Princess Daphne bought three necklaces and a set of earrings for a total of $240,000. If all three necklaces were equal in price, and the earrings were three times as expensive as any one necklace, then how expensive was the cost of a single necklace?"""
    # Define the total cost and the number of necklaces
    total_cost = 240000
    num_necklaces = 3

    # Calculate the cost of the earrings
    earrings_cost = num_necklaces * 3

    # Calculate the cost of the necklaces
    necklace_cost = (total_cost - earrings_cost) / num_necklaces

    # return the result
    result = int(necklace_cost)
    return result

print(solution())