def solution():
    snes_value = 150
    trade_in_percent = 0.8
    cash_paid = 80
    change_received = 10
    game_value = 30

    # Calculate the amount of cash Tom received for his SNES trade-in
    snes_trade_in_value = snes_value * trade_in_percent

    # Calculate the total amount of money Tom paid (including trade-in value and change received)
    total_paid = snes_trade_in_value + cash_paid - change_received + game_value

    # Calculate the cost of the NES gaming system
    nes_price = total_paid
    result = nes_price
    return result

print(solution())