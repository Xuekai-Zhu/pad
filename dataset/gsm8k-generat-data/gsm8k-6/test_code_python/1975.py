def solution():
    # Calculate the amount of money in the account after 1 year with 20% interest
    year_1 = 1000 * 1.2  # $1,000 with a 20% interest rate

    # Calculate the amount of money after taking out half to buy a new TV
    after_TV = year_1/2  # taking out half the money

    # Calculate the amount of money after 1 year with 15% interest on the remaining money
    year_2 = after_TV * 1.15  # remaining money with a 15% interest rate

    result = year_2
    return result

print(solution())