def solution():
    """Snap, Crackle, and Pop spend $150 on cereal in a grocery store. Snap spends twice as much as Crackle. Crackle spends 3 times as much as Pop. How much did Pop spend?"""
    # Define the amount Pop spent as x
    x = None

    # Calculate the amount Crackle spent, which is 3 times less than Snap's spending, and Snap spent twice the amount of Crackle
    crackle_spending = (150 / 7)
    snap_spending = 2 * crackle_spending

    # Calculate the amount Pop spent, which is 3 times less than Crackle
    x = crackle_spending / 3

    result = round(x)
    return result

print(solution())