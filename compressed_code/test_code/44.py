def solution():
    
    total_earnings = 28
    milkshake_cost = total_earnings / 7
    remaining_money = total_earnings - milkshake_cost
    savings_account = remaining_money / 2
    remaining_in_wallet = remaining_money - savings_account - 1
    lost_money = remaining_in_wallet
    result = lost_money
    return result

print(solution())