def solution():
    """If Alice purchased 3600 acorns for nine times the price Bob paid, and Bob paid $6000 for his acorns, how much money did Alice pay for each acorn?"""
    # Define the price Bob paid for his acorns
    bob_price = 6000

    # Calculate the total amount Alice paid for her acorns
    alice_total = 3600 * 9 * bob_price

    # Calculate the price Alice paid per acorn
    alice_price = alice_total / 3600

    result = alice_price
    return result

print(solution())