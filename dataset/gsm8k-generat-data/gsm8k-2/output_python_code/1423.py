def solution():
    """Christian and Sue wanted to get a $50.00 bottle of perfume for their mom for her birthday. Christian had $5.00 saved up and Sue had $7.00. Christian then mowed 4 of his neighbors' yards, charging $5.00 each, while Sue walked 6 dogs for her neighbors, charging $2.00 per dog. How much more money will Christian and Sue need to make in order to buy the bottle of perfume for their mom?"""
    perfume_price = 50
    christian_money = 5 + 4 * 5
    sue_money = 7 + 6 * 2
    total_money = christian_money + sue_money
    remaining_money = perfume_price - total_money
    result = remaining_money
    return result

print(solution())