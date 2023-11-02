def solution():
    """Christian and Sue wanted to get a $50.00 bottle of perfume for their mom for her birthday.  Christian had $5.00 saved up and Sue had $7.00.  Christian then mowed 4 of his neighbors' yards, charging $5.00 each, while Sue walked 6 dogs for her neighbors, charging $2.00 per dog.  How much more money will Christian and Sue need to make in order to buy the bottle of perfume for their mom?"""
    # Define the cost of the perfume and the amount of money Christian and Sue have
    PERFUME_COST = 50
    CHRISTIAN_MONEY = 5
    SUE_MONEY = 7

    # Calculate the amount of money Christian and Sue earned from their jobs
    christian_earnings = 4 * 5
    sue_earnings = 6 * 2

    # Calculate the total amount of money Christian and Sue have
    total_money = christian_earnings + sue_earnings + CHRISTIAN_MONEY + SUE_MONEY

    # Calculate the remaining amount needed to buy the perfume
    remaining_money = PERFUME_COST - total_money

    # Display the remaining amount needed
    result = remaining_money
    return result

print(solution())