def solution():
    """Emma bought 3 dozens of macarons in addition to her 10 pieces of macarons for a party. If 15 pieces of macarons are left over, how many pieces of macarons were eaten?"""
    dozens_bought = 3
    pieces_bought = dozens_bought * 12 + 10
    pieces_left_over = 15
    pieces_eaten = pieces_bought - pieces_left_over
    result = pieces_eaten
    return result

print(solution())