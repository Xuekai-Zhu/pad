def solution():
    """A crate can hold 20 kilograms of tomatoes. Tommy has 3 crates which he bought for $330. He wants to sell the tomatoes for $6 per 1 kilogram but 3 kilograms of tomatoes were rotten. How much will be Tommy's profit from selling those tomatoes?"""
    max_weight_per_crate = 20  # in kg
    num_crates = 3
    cost_of_crates = 330  # in dollars
    price_per_kg = 6  # in dollars
    rotten_tomatoes_weight = 3  # in kg

    max_total_weight = max_weight_per_crate * num_crates
    total_weight = max_total_weight - rotten_tomatoes_weight
    total_profit = (total_weight * price_per_kg) - cost_of_crates

    result = total_profit
    return result

print(solution())