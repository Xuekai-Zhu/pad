def solution():
    # Define the number of nickels as n and the number of dimes as d
    # Use the given relationship between n and d to solve for n in terms of d
    d = n + 4
    # Use the given total value of the coins to set up an equation in terms of n
    5n + 10d = 70
    # Substitute n + 4 for d and solve for n
    5n + 10(n + 4) = 70
    15n + 40 = 70
    15n = 30
    n = 2

    # Return the number of nickels
    result = n
    return result

print(solution())