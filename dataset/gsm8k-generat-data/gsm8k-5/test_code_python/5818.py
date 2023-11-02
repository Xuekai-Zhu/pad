def solution():
    quarters = 4  # Tommy has 4 quarters
    pennies = 10 * quarters  # Tommy has 10 times as many pennies as quarters
    dimes = pennies + 10  # Tommy has 10 more dimes than pennies
    nickels = 2 * dimes  # Tommy has twice as many nickels as dimes

    result = nickels
    return result

print(solution())