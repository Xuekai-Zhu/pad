def solution():
    """Rocco stores his coins in piles of 10 coins each. He has 4 piles of quarters, 6 piles of dimes, 9 piles of nickels, and 5 piles of pennies. How much money does Rocco have?"""
    quarters = 4 * 10 * 0.25
    dimes = 6 * 10 * 0.1
    nickels = 9 * 10 * 0.05
    pennies = 5 * 10 * 0.01
    total_money = quarters + dimes + nickels + pennies
    result = total_money
    return result

print(solution())