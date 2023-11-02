def solution():
    cost_price = 0.25  # The cost price of one goldfish is $0.25
    selling_price = 0.75  # The selling price of one goldfish is $0.75
    tank_price = 100  # The price of the new tank is $100

    # Calculate the profit per goldfish
    profit_per_fish = selling_price - cost_price

    # Calculate the number of goldfish needed to cover the cost of the tank
    fish_for_tank = tank_price / profit_per_fish

    # Calculate the total number of goldfish sold
    total_fish_sold = fish_for_tank / 0.55  # The owner is 45% short of the price, so he has only 55% of the required amount

    result = total_fish_sold
    return result

print(solution())