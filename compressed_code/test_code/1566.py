def solution():
    
    board_game_cost = 15
    total_cost = board_game_cost * 6
    amount_paid = 100
    change = amount_paid - total_cost
    number_of_bills = change / 5
    result = int(number_of_bills)
    return result

print(solution())