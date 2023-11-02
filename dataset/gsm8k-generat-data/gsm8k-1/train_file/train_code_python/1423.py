def solution():
    """Christian and Sue wanted to get a $50.00 bottle of perfume for their mom for her birthday. Christian had $5.00 saved up and Sue had $7.00. Christian then mowed 4 of his neighbors' yards, charging $5.00 each, while Sue walked 6 dogs for her neighbors, charging $2.00 per dog. How much more money will Christian and Sue need to make in order to buy the bottle of perfume for their mom?"""
    perfume_cost = 50
    christian_savings = 5
    sue_savings = 7
    christian_mowed = 4
    christian_earnings = christian_mowed * 5
    sue_walked = 6
    sue_earnings = sue_walked * 2
    total_money = christian_savings + sue_savings + christian_earnings + sue_earnings
    remaining_money = perfume_cost - total_money
    result = remaining_money
    return result

print(solution())