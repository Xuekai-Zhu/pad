def solution():
    num_polo_shirts = 3
    polo_shirt_price = 26

    num_necklaces = 2
    necklace_price = 83

    computer_game_price = 90

    rebate = 12

    # Calculate the total cost of all polo shirts
    total_polo_shirt_cost = num_polo_shirts * polo_shirt_price

    # Calculate the total cost of all necklaces
    total_necklace_cost = num_necklaces * necklace_price

    # Calculate the total cost of all gifts before rebate
    total_cost_before_rebate = total_polo_shirt_cost + total_necklace_cost + computer_game_price

    # Calculate the total cost of all gifts after rebate
    total_cost_after_rebate = total_cost_before_rebate - rebate
    result = total_cost_after_rebate
    return result

print(solution())