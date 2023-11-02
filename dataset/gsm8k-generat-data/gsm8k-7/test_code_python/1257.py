def solution():
    initial_investment = 2000

    # Alice doubles her money in the stock market
    alice_money = initial_investment * 2

    # Bob makes 5 times more money than he invested
    bob_money = initial_investment * 5

    # Calculate the difference between Bob's and Alice's money
    difference = bob_money - alice_money
    result = difference
    return result

print(solution())