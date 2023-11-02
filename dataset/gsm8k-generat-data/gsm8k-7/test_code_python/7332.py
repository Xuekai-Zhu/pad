def solution():
    num_first_pieces = 3
    total_first_pieces_price = 45000

    # Calculate the price of each of the first three pieces of art
    price_per_first_piece = total_first_pieces_price / num_first_pieces

    # Calculate the price of the fourth piece, which is 50% more expensive than the first three
    price_of_fourth_piece = price_per_first_piece * 1.5

    # Calculate the total cost of all four pieces of art
    total_cost = total_first_pieces_price + price_of_fourth_piece
    result = total_cost
    return result

print(solution())