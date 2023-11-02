def solution():
    """Darrel has 76 quarters, 85 dimes, 20 nickels and 150 pennies. If he drops all of his money into a coin-counting machine, they will convert his change into dollars for a 10% fee. How much will he receive after the 10% fee?"""
    quarters = 76
    dimes = 85
    nickels = 20
    pennies = 150
    total_money = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)
    fee = total_money * 0.1
    money_after_fee = total_money - fee
    result = money_after_fee
    return result

print(solution())