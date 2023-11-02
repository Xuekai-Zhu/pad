def solution():
    # Calculate the trade-in value of the SNES
    snes_trade_in = 150 * 0.8

    # Calculate the total amount Tom paid
    total_paid = snes_trade_in + 80 - 10 + 30

    # Calculate the cost of the NES
    nes_cost = total_paid - snes_trade_in

    result = nes_cost
    return result

print(solution())