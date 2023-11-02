def solution():
    """Tom needs to buy a new gaming system. He trades in his super Nintendo for an original NES. The SNES is worth $150 and the store gives him 80% of that value. He gives $80 and gets back $10 change and a game worth $30. How much was the NES on sale for?"""
    # Calculate the amount of money Tom got from trading in his SNES
    snes_value = 150
    trade_in_value = snes_value * 0.8

    # Calculate the total amount of money Tom spent
    spent = trade_in_value + 80 - 10 + 30

    # Calculate the cost of the NES
    nes_price = spent - trade_in_value

    result = nes_price
    return result

print(solution())