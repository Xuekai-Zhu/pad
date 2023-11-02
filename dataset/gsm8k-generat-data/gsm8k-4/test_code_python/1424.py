def solution():
    """Christian and Sue wanted to get a $50.00 bottle of perfume for their mom for her birthday. Christian had $5.00 saved up and Sue had $7.00. Christian then mowed 4 of his neighbors' yards, charging $5.00 each, while Sue walked 6 dogs for her neighbors, charging $2.00 per dog. How much more money will Christian and Sue need to make in order to buy the bottle of perfume for their mom?"""
    # Define the cost of the perfume and the money Christian and Sue already have
    perfume_cost = 50
    christian_money = 5
    sue_money = 7

    # Calculate the money earned by Christian and Sue
    christian_money += 5 * 4
    sue_money += 2 * 6

    # Calculate the total money they have
    total_money = christian_money + sue_money

    # Calculate the remaining amount they need to buy the perfume
    remaining_money = perfume_cost - total_money

    result = remaining_money
    return result

print(solution())