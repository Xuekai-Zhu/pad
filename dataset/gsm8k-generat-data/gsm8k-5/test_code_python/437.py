def solution():
    chicken_price = 1.5  # Lao can sell each chicken for $1.50
    feed_price = 2  # A bag of chicken feed costs $2 and weighs 20 pounds
    feed_per_chicken = 2  # Each chicken needs 2 pounds of feed from hatch to sale
    total_profit = 65  # Lao makes a profit of $65 from selling chickens

    # Calculate the number of chickens Lao sold
    chicken_count = 0
    feed_cost = 0
    while chicken_price * chicken_count - feed_cost < total_profit:
        chicken_count += 1
        feed_cost = feed_price * (chicken_count * feed_per_chicken) / 20

    result = chicken_count
    return result

print(solution())