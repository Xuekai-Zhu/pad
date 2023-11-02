def solution():
    # Calculate the price of each of the first 3 pieces
    price_per_piece = 45000 / 3

    # Calculate the price of the 4th piece, which is 50% more expensive than the first 3
    price_4th_piece = price_per_piece * 1.5

    # Calculate the total cost of all the art
    total_cost = (price_per_piece * 3) + price_4th_piece
    result = total_cost
    return result

print(solution())