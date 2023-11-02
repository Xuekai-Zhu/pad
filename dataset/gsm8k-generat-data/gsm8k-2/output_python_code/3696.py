def solution():
    """Opal won $100.00 betting on a horse race. She put half of her winnings into savings and bet the other half of her winnings. This time, she made a 60% profit and again, put half of her earnings into savings. How much did she put into her savings?"""
    initial_winnings = 100
    first_half = initial_winnings / 2
    second_half = initial_winnings / 2
    second_half_profit = 0.6 * second_half
    second_half_earnings = second_half + second_half_profit
    second_half_savings = second_half_earnings / 2
    total_savings = first_half + second_half_savings
    result = total_savings
    return result

print(solution())