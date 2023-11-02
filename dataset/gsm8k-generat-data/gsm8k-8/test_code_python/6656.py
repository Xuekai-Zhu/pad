def solution():
    # Calculate the profit per goldfish
    profit_per_fish = 0.75 - 0.25

    # Calculate the total profit needed for the tank
    total_profit_needed = 100 * 1.45

    # Calculate the number of goldfish needed to make the total profit
    num_goldfish_needed = total_profit_needed / profit_per_fish

    result = int(num_goldfish_needed)
    return result

print(solution())