def solution():
    """Lao is farming chickens. He can sell each chicken for $1.50. A bag of chicken feed weighs 20 pounds and costs $2. Each chicken will need 2 pounds of feed from the time it hatches to the time he sells it. If he makes $65 profit from selling chickens, how many did he sell?"""
    # Define the price per chicken and the cost of each bag of feed
    CHICKEN_PRICE = 1.5
    FEED_COST = 2

    # Define the amount of feed required for each chicken
    FEED_PER_CHICKEN = 2

    # Define the total profit made from selling chickens
    total_profit = 65

    # Calculate the number of bags of feed used
    bags_of_feed = total_profit / FEED_COST

    # Calculate the total weight of feed used
    total_feed_weight = bags_of_feed * 20

    # Calculate the number of chickens he was able to raise with the feed
    total_chickens = total_feed_weight / FEED_PER_CHICKEN

    # Calculate the total profit from selling the chickens
    total_sales = total_chickens * CHICKEN_PRICE

    # Calculate the final profit, accounting for the cost of the feed
    final_profit = total_sales - (bags_of_feed * FEED_COST)

    # Display the number of chickens sold
    result = round(total_chickens)
    return result

print(solution())