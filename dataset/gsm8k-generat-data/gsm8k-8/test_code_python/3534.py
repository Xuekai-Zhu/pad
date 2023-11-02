def solution():
    # Define variables
    num_quarters = 0
    num_dimes = 0
    num_nickels = 0
    total_coins = 63

    # Set up equations
    # d = q + 3
    # n = q - 6
    # q + d + n = 63

    # Simplify and solve system of equations
    # q + q + 3 + q - 6 = 63
    # 3q - 3 = 63
    # 3q = 66
    # q = 22

    num_quarters = 22
    num_dimes = num_quarters + 3
    num_nickels = num_quarters - 6

    result = num_quarters
    return result

print(solution())