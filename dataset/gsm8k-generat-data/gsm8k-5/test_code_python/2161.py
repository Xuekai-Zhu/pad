def solution():
    initial_balance = 10  # Renata had $10 to spend initially
    donation = 4
    charity_prize = 90
    slot_losses = 50 + 10 + 5
    gas_station_spending = 1 + 1
    lottery_winnings = 65

    # Calculate Renata's final balance
    final_balance = initial_balance - donation + charity_prize - slot_losses - gas_station_spending + lottery_winnings
    result = final_balance
    return result

print(solution())