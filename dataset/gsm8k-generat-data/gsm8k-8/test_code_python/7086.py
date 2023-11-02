def solution():
    # Calculate the amount earned from selling popcorn for 5 days
    popcorn_earnings = 50 * 5

    # Calculate the amount earned from selling cotton candy for 5 days (3 times the amount of popcorn earnings)
    cotton_candy_earnings = popcorn_earnings * 3

    # Calculate the total earnings for 5 days
    total_earnings = popcorn_earnings + cotton_candy_earnings

    # Subtract the rent and ingredient cost from the total earnings to get the net profit
    net_profit = total_earnings - 30 - 75
    result = net_profit
    return result

print(solution())