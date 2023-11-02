def solution():
    total_winnings = 100.0  # Opal won $100.00
    first_half = total_winnings / 2  # Opal put half of her winnings into savings
    remaining_half = total_winnings - first_half  # Opal bet the other half of her winnings

    # Calculate Opal's earnings from her bet
    bet_earnings = remaining_half * 0.6
    second_half = bet_earnings / 2  # Opal put half of her earnings into savings

    total_savings = first_half + second_half  # Calculate Opal's total savings
    result = total_savings
    return result

print(solution())