def solution():
    """Lao is farming chickens. He can sell each chicken for $1.50. A bag of chicken feed weighs 20 pounds and costs $2. Each chicken will need 2 pounds of feed from the time it hatches to the time he sells it. If he makes $65 profit from selling chickens, how many did he sell?"""
    chicken_price = 1.5
    feed_weight = 20
    feed_cost = 2
    feed_per_chicken = 2

    # Calculate the number of chickens sold based on the profit made
    chicken_count = int((65/feed_per_chicken)/chicken_price)

    # Calculate the total cost of the feed for all the chickens
    total_feed_cost = chicken_count * feed_cost * (feed_weight/feed_per_chicken)

    # Calculate the total profit made by selling the chickens
    total_profit = chicken_count * chicken_price - total_feed_cost

    result = chicken_count
    return result

print(solution())