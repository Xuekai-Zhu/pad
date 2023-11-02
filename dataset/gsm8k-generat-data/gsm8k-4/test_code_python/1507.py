def solution():
    """Sean has 4 dollars more than half as much money as Fritz. Rick has 3 times as much money as Sean. If Fritz has 40 dollars, how much money do Rick and Sean have?"""
    # Define Fritz's money
    fritz_money = 40

    # Calculate Sean's money
    sean_money = fritz_money / 2 + 4

    # Calculate Rick's money
    rick_money = sean_money * 3

    # Return the total money of Rick and Sean
    result = rick_money + sean_money
    return result

print(solution())