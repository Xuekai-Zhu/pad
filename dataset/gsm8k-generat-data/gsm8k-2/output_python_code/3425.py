def solution():
    """Lorie has 2 pieces of $100 bills. He requested to change one piece of the $100 bills into $50 bills. Half of the remaining $100 bill is changed to $10 bills while the rest is changed to $5 bills. How many pieces of bills will she have?"""
    # Initially, Lorie has 2 pieces of $100 bills, which is equivalent to $200.
    total_money = 200

    # One piece of $100 bill is changed to $50 bills, which gives Lorie $50 x 2 = $100.
    total_money += 100

    # Half of the remaining $100 bill (i.e. $100) is changed to $10 bills, which gives Lorie $50 x 2 = $100.
    total_money += (100 / 2) * 10

    # The other half of the $100 bill is changed to $5 bills, which gives Lorie $50 x 2 = $100.
    total_money += (100 / 2) * 5

    # Lorie will have a total of 10 pieces of bills (3 pieces of $100 bills, 4 pieces of $10 bills, and 3 pieces of $5 bills).
    result = 10
    return result

print(solution())