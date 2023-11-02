def solution():
    """Tom needs to buy a new gaming system.  He trades in his super Nintendo for an original NES.  The SNES is worth $150 and the store gives him 80% of that value.  He gives $80 and gets back $10 change and a game worth $30.  How much was the NES on sale for?"""
    # Calculate the value of the SNES trade-in
    snes_value = 150 * 0.8

    # Calculate the total amount paid by Tom
    total_paid = 80 - 10 + 30 + snes_value

    # Calculate the cost of the NES
    nes_cost = total_paid - snes_value

    # Display the cost of the NES
    result = nes_cost
    return result

print(solution())