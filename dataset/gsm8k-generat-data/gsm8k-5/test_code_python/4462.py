def solution():
    weight_per_bar = 1.5  # Each bar of soap weighs 1.5 pounds
    price_per_pound = 0.5  # John paid $.5 per pound for the soap
    total_bars = 20  # John bought 20 bars of soap

    # Calculate the total weight of the soap
    total_weight = weight_per_bar * total_bars

    # Calculate how much money John spent on soap
    total_cost = total_weight * price_per_pound
    result = total_cost
    return result

print(solution())