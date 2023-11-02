def solution():
    # Let's assume that Steve is holding "n" number of nickels
    # Steve has "4 more dimes than nickels"
    # So, he will have "n+4" number of dimes

    # The total value of nickels = 5*n cents
    # The total value of dimes = 10*(n+4) cents

    # Steve has a total of 70 cents in his hand
    # So, 5*n + 10*(n+4) = 70

    # Solving the above equation for "n", we get:
    n = 3

    result = n
    return result

print(solution())