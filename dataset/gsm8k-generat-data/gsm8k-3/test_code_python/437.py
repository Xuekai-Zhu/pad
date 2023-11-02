def solution():
    """Lao is farming chickens. He can sell each chicken for $1.50. A bag of chicken feed weighs 20 pounds and costs $2. Each chicken will need 2 pounds of feed from the time it hatches to the time he sells it. If he makes $65 profit from selling chickens, how many did he sell?"""
    # Define the selling price and cost of feed per bag
    SELLING_PRICE = 1.5
    FEED_COST = 2

    # Calculate the cost of feed per chicken
    feed_cost_per_chicken = (FEED_COST / 20) * 2

    # Calculate the profit per chicken
    profit_per_chicken = SELLING_PRICE - feed_cost_per_chicken

    # Calculate the number of chickens sold
    number_of_chickens_sold = int(65 / profit_per_chicken)

    # Display the number of chickens sold
    result = number_of_chickens_sold
    return result

print(solution())