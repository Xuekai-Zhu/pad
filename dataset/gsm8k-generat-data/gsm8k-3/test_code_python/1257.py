def solution():
    """Alice and Bob are each given $2000 to invest. Alice puts all of her money in the stock market and doubles her money. Bob invests in real estate and makes five times more money than he invested. How much more money does Bob have now than Alice?"""
    # Define the initial investments
    alice_investment = 2000
    bob_investment = 2000

    # Calculate Alice's earnings
    alice_earnings = alice_investment * 2

    # Calculate Bob's earnings
    bob_earnings = bob_investment * 5

    # Calculate the difference in earnings
    difference = bob_earnings - alice_earnings

    # Display the difference in earnings
    result = difference
    return result

print(solution())