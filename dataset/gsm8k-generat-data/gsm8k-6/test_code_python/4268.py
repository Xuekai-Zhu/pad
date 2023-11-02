def solution():
    # Calculate how much Derek spent on lunch
    derek_spent = 14 + 11 + 5
    # Calculate how much money Derek has left after buying lunch
    derek_money_left = 40 - derek_spent
    # Calculate how much money Dave has left after buying lunch
    dave_money_left = 50 - 7
    # Calculate the difference between how much money Dave and Derek have left
    difference = dave_money_left - derek_money_left
    result = difference
    return result

print(solution())