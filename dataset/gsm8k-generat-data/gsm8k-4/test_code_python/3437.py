def solution():
    """John receives $100 from his uncle and gives his sister Jenna 1/4 of that money. He goes and buys groceries worth $40. How much money does John have remaining?"""
    # Define the initial amount John receives
    initial_amount = 100

    # Calculate the amount Jenna receives
    jenna_amount = initial_amount * 1/4

    # Calculate the amount John has left after giving money to Jenna and buying groceries
    remaining_amount = initial_amount - jenna_amount - 40

    # return the result
    result = remaining_amount
    return result

print(solution())