def solution():
    """Darrel has 76 quarters, 85 dimes, 20 nickels and 150 pennies. If he drops all of his money into a coin-counting machine, they will convert his change into dollars for a 10% fee. How much will he receive after the 10% fee?"""
    quarters_value = 0.25
    dimes_value = 0.10
    nickels_value = 0.05
    pennies_value = 0.01
    total_cents = (76 * quarters_value) + (85 * dimes_value) + (20 * nickels_value) + (150 * pennies_value)
    total_dollars = total_cents / 100
    fee = total_dollars * 0.1
    total_after_fee = total_dollars - fee
    result = total_after_fee
    return result

print(solution())