def solution():
    """Alice and Bob are each given $2000 to invest. Alice puts all of her money in the stock market and doubles her money. Bob invests in real estate and makes five times more money than he invested. How much more money does Bob have now than Alice?"""
    alice_money = 2000
    alice_profit = alice_money
    bob_money = 2000
    bob_profit = 5 * bob_money - bob_money
    total_alice = alice_money + alice_profit
    total_bob = bob_money + bob_profit
    difference = total_bob - total_alice
    result = difference
    return result

print(solution())