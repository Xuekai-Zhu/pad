def solution():
    """Abigail spent 60% of her money on food, and 25% of the remainder on her phone bill. After spending $20 on entertainment, she is left with $40. How much money did Abigail have initially?"""
    # Let x be the amount of money Abigail had initially
    # Abigail spent 60% of her money on food, so she has 40% remaining
    remaining_money = x * 0.4

    # Abigail spent 25% of the remaining money on her phone bill
    phone_bill = remaining_money * 0.25

    # After the phone bill and entertainment expenses, Abigail is left with $40
    remaining_money -= phone_bill + 20 + 40

    # So, we have an equation: remaining_money = 0.4x - 0.25(0.4x) - 60
    # Simplifying it:
    remaining_money = 0.85 * 0.4 * x - 60

    # Solving for x:
    x = (remaining_money + 60) / (0.85 * 0.4)

    # Display the initial amount of money Abigail had
    result = x
    return result

print(solution())