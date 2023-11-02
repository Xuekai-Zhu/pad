def solution():
    """Millie decides to open a lemonade stand. She spends $18 to buy enough supplies to make 3 pitchers of lemonade. Each pitcher holds 12 cups of lemonade. She sells each cup of lemonade for $1. She sells an average of 4 cups per hour that her lemonade stand is open. If Millie sells all of the lemonade, how much profit will she make per hour that she spends running the lemonade stand?"""
    cost_per_pitcher = 18 / 3
    cups_per_pitcher = 12
    price_per_cup = 1
    cups_sold_per_hour = 4
    profit_per_pitcher = (cups_per_pitcher * price_per_cup) - cost_per_pitcher
    profit_per_hour = profit_per_pitcher / (cups_per_pitcher / cups_sold_per_hour)
    result = profit_per_hour
    return result

print(solution())