def solution():
    derek_money = 40
    derek_spent = 14 + 11 + 5
    dave_money = 50
    dave_spent = 7

    # Calculate how much money Derek has left
    derek_left = derek_money - derek_spent

    # Calculate how much money Dave has left
    dave_left = dave_money - dave_spent

    # Calculate the difference in money between Dave and Derek
    difference = dave_left - derek_left
    result = difference
    return result

print(solution())