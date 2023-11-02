def solution():
    """Alice and Bob are each given $2000 to invest. Alice puts all of her money in the stock market and doubles her money. Bob invests in real estate and makes five times more money than he invested. How much more money does Bob have now than Alice?"""
    # Define the initial investment amount for Alice and Bob
    alice_investment = 2000
    bob_investment = 2000

    # Calculate the final amount for Alice and Bob
    alice_final = alice_investment * 2
    bob_final = bob_investment * 6  # 5 times more money than invested, plus the initial investment

    # Calculate the difference in money between Bob and Alice
    difference = bob_final - alice_final

    # return the result
    result = difference
    return result

print(solution())