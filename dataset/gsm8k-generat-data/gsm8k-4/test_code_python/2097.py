def solution():
    """Ali, Nada, and John have a total of $67 in their wallets. Ali has $5 less than Nada and John has 4 times more than Nada. How much money does John have?"""
    # Define the total amount of money
    total_money = 67

    # Let x be the amount of money Nada has
    # Ali has $5 less than Nada
    # John has 4 times more than Nada
    x = (total_money - 5) / (1 + 1 + 4)

    # Calculate the amount of money John has
    john_money = 4 * x

    result = john_money
    return result

print(solution())