def solution():
    num_gum_packs = 2
    num_candy_bars = 3
    gum_price = 0.75  # Half the price of a candy bar

    candy_bar_price = 1.5

    # Calculate the total cost of all gum packs
    total_gum_cost = num_gum_packs * gum_price

    # Calculate the total cost of all candy bars
    total_candy_bar_cost = num_candy_bars * candy_bar_price

    # Calculate the total cost of all items
    total_cost = total_gum_cost + total_candy_bar_cost
    result = total_cost
    return result

print(solution())