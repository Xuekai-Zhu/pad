def solution():
    cost_price = 0.25
    selling_price = 0.75
    tank_cost = 100
    shortfall = 0.45
    profit_per_fish = selling_price - cost_price

    # Calculate the total profit needed to buy the tank
    target_profit = tank_cost / (1 - shortfall)

    # Calculate the number of fish needed to make the target profit
    num_fish = target_profit / profit_per_fish
    result = int(num_fish)
    return result

print(solution())