def solution():
    original_winnings = 100.0
    first_half = original_winnings / 2.0
    second_half_bet = first_half

    # Calculate the winnings from the bet
    second_half_winnings = second_half_bet * 0.6

    # Calculate the total amount in savings
    total_savings = (first_half / 2.0) + (second_half_winnings / 2.0)
    result = total_savings
    return result

print(solution())