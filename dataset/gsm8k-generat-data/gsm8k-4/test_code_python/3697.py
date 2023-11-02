def solution():
    """Opal won $100.00 betting on a horse race. She put half of her winnings into savings and bet the other half of her winnings. This time, she made a 60% profit and again, put half of her earnings into savings. How much did she put into her savings? """
    # Define the initial winnings and the amount put into savings
    initial_winnings = 100
    savings_amount = initial_winnings / 2

    # Calculate the amount won in the second bet
    second_bet_winnings = initial_winnings / 2
    second_bet_profit = 0.6 * second_bet_winnings
    second_bet_winnings += second_bet_profit

    # Calculate the amount put into savings from the second bet
    savings_amount += second_bet_winnings / 2

    result = savings_amount
    return result

print(solution())