def solution():
    
    polo_shirt_cost = 26
    necklace_cost = 83
    computer_game_cost = 90
    polo_shirt_total = 3 * polo_shirt_cost
    necklace_total = 2 * necklace_cost
    subtotal = polo_shirt_total + necklace_total + computer_game_cost
    total_cost = subtotal - 12
    result = total_cost
    return result

print(solution())