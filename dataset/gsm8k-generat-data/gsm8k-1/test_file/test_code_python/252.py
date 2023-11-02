def solution():
    """Brady is counting the money in his piggy bank. He has 100 pennies, 40 nickels, 20 dimes, and 40 pieces of dollar bills. How much does Brady have in his piggy bank in dollars?"""
    pennies_value = 0.01
    nickels_value = 0.05
    dimes_value = 0.1
    dollars_value = 1
    total = (100 * pennies_value) + (40 * nickels_value) + (20 * dimes_value) + (40 * dollars_value)
    result = total
    return result

print(solution())