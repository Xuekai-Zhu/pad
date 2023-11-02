def solution():
    """Jason waits on a customer whose check comes to $15.00. Jason's state applies a 20% tax to restaurant sales. If the customer gives Jason a $20 bill and tells him to keep the change, how much is Jason's tip?"""
    # Calculate the tax on the restaurant sales
    tax = 0.2 * 15.00

    # Calculate the total amount owed by the customer
    total = 15.00 + tax

    # Calculate the amount of change the customer receives from a $20 bill
    change = 20.00 - total

    # Calculate the tip Jason receives, which is the amount of change
    tip = change

    result = tip
    return result

print(solution())