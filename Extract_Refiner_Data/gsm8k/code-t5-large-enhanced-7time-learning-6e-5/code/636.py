def solution():
    
    base_price = 30000
    king_cab_price = 7500
    leather_price = king_cab_price / 3
    running_board_price = leather_price - 500
    total_price = base_price + king_cab_price + leather_price + running_board_price
    result = total_price
    return result

print(solution())