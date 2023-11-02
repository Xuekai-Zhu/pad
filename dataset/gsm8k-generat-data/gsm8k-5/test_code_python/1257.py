def solution():
    alice_initial_investment = 2000
    bob_initial_investment = 2000

    alice_earnings = alice_initial_investment * 2  # Alice doubles her money in the stock market
    bob_earnings = bob_initial_investment * 5  # Bob makes five times more money than he invested in real estate

    difference = bob_earnings - alice_earnings
    result = difference
    return result

print(solution())