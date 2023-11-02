def solution():
    
    starting_amount = 25
    amount_given_to_mom = 8
    remaining_amount = starting_amount - amount_given_to_mom
    money_market_amount = remaining_amount * 0.5
    items_cost = 5 * 0.5
    final_amount = remaining_amount - money_market_amount - items_cost
    result = final_amount
    return result

print(solution())