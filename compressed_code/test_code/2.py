def solution():
    
    wallet_price = 100
    current_savings = wallet_price / 2
    parents_help = 15
    grandparents_help = 2 * parents_help
    total_money = current_savings + parents_help + grandparents_help
    needed_money = wallet_price - total_money
    result = needed_money
    return result

print(solution())