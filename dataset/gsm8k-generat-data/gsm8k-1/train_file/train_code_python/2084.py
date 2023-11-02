def solution():
    """Tom needs to buy a new gaming system. He trades in his super Nintendo for an original NES. The SNES is worth $150 and the store gives him 80% of that value. He gives $80 and gets back $10 change and a game worth $30. How much was the NES on sale for?"""
    snes_value = 150
    store_value = snes_value * 0.8
    total_paid = store_value + 10 + 30
    nes_price = total_paid - 80
    result = nes_price
    return result

print(solution())