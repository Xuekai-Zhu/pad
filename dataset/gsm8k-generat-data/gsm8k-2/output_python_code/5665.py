def solution():
    """Steve is holding nickels and dimes in his hand. He has 4 more dimes than nickels. He has a total of 70 cents in his hand. How many nickels is he holding?"""
    total_cents = 70
    nickel_value = 5
    dime_value = 10

    # Set up equations
    # Let n be the number of nickels and d be the number of dimes
    # d = n + 4  (Steve has 4 more dimes than nickels)
    # 10d + 5n = 70  (The total value of his coins is 70 cents)

    # Substitute d = n + 4 into the second equation
    # 10(n+4) + 5n = 70
    # 15n + 40 = 70
    # 15n = 30
    # n = 2

    result = 2  # Steve is holding 2 nickels
    return result

print(solution())