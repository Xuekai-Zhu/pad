def solution():
    """Lao is farming chickens. He can sell each chicken for $1.50. A bag of chicken feed weighs 20 pounds and costs $2. Each chicken will need 2 pounds of feed from the time it hatches to the time he sells it. If he makes $65 profit from selling chickens, how many did he sell?"""
    chicken_price = 1.50
    feed_bag_weight = 20
    feed_bag_cost = 2
    feed_per_chicken = 2
    total_feed_cost = feed_bag_cost / (feed_bag_weight / feed_per_chicken)
    total_profit = 65
    chicken_sales = total_profit / (chicken_price - (total_feed_cost / 2))
    result = chicken_sales
    return result

print(solution())