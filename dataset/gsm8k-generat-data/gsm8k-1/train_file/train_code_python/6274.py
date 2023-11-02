def solution():
    """Tanesha needs to buy rope so cut into 10 pieces that are each six inches long. She sees a 6-foot length of rope that cost $5 and also sees 1-foot lengths of rope that cost $1.25 each. What is the least she has to spend to get the rope she needs?"""
    ten_piece_length = (10 * 6) / 12 # Convert from inches to feet
    six_foot_length = 6
    six_foot_price = 5
    one_foot_length = 1
    one_foot_price = 1.25
    if ten_piece_length > six_foot_length:
        length_needed = ten_piece_length
        price_needed = six_foot_price
    else:
        length_needed = ten_piece_length
        price_needed = one_foot_price
    
    num_pieces_needed = length_needed / one_foot_length
    cost = num_pieces_needed * price_needed
    result = cost
    return result

print(solution())