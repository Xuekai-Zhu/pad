def solution():
    # Let's assign 'n' as the number of nickels and 'd' as the number of dimes
    # as per the given problem, he has 4 more dimes than nickels
    # i.e d = n + 4

    # let's calculate total value in cents
    # as one nickel = 5 cents and one dime = 10 cents
    # total_value = 5n + 10d
    # substituting value of 'd' from above equation, we get:
    # total_value = 5n + 10(n+4)
    # total_value = 15n + 40

    # as per the problem, total value in cents is 70 cents
    # i.e total_value = 70
    # substituting values, we get:
    # 15n + 40 = 70
    # 15n = 30
    # n = 2

    # So, Steve is holding 2 nickels
    result = 2
    return result

print(solution())