def solution():
    """If Alice purchased 3600 acorns for nine times the price Bob paid, and Bob paid $6000 for his acorns, how much money did Alice pay for each acorn?"""
    # Calculate the total price that Alice paid for the acorns
    alice_price = 3600 * 9 * 6000

    # Calculate the price per acorn for Alice
    acorn_price = alice_price / 3600

    # Display the price per acorn that Alice paid
    result = acorn_price
    return result

print(solution())