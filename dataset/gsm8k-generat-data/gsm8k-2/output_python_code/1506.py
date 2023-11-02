def solution():
    """Sean has 4 dollars more than half as much money as Fritz. Rick has 3 times as much money as Sean. If Fritz has 40 dollars, how much money do Rick and Sean have?"""
    fritz_money = 40
    sean_money = (fritz_money / 2) + 4
    rick_money = 3 * sean_money
    total_money = rick_money + sean_money
    result = total_money
    return result

print(solution())