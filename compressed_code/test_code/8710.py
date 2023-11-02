def solution():
    
    initial_winnings = 100
    first_half = initial_winnings / 2
    second_half = initial_winnings / 2
    second_half_profit = second_half * 0.6
    second_half_earnings = second_half + second_half_profit
    second_half_savings = second_half_earnings / 2
    total_savings = first_half + second_half_savings
    result = total_savings
    return result

print(solution())