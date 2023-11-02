def solution():
    """At the bake sale, Tamara makes $32 from the brownies. She made 2 pans of brownies which were all sold. The brownies were cut into 8 big square pieces. How much did each brownie cost?"""
    total_profit = 32
    num_pans = 2
    num_pieces = num_pans * 8
    price_per_piece = total_profit / num_pieces
    result = price_per_piece
    
    return result

print(solution())