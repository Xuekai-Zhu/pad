def solution():
    # Calculate the amount Tom receives for trading in the SNES
    snes_trade_in = 150 * 0.8  # The store gives him 80% of the SNES value

    # Calculate the total amount Tom pays for the NES and game
    total_payment = 80 - 10 + 30  # Tom pays $80 and gets back $10 change and a $30 game

    # Calculate the cost of the NES
    nes_cost = total_payment - snes_trade_in
    result = nes_cost
    return result

print(solution())