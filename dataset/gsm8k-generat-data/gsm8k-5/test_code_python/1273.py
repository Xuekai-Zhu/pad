def solution():
    candy_bar_cost = 1.5  # Each candy bar costs $1.5
    gum_cost = candy_bar_cost / 2  # Each pack of gum costs half as much as a candy bar
    num_gum_packs = 2  # John buys 2 packs of gum
    num_candy_bars = 3  # John buys 3 candy bars

    # Calculate the total cost of the gum packs
    total_gum_cost = gum_cost * num_gum_packs

    # Calculate the total cost of the candy bars
    total_candy_cost = candy_bar_cost * num_candy_bars

    # Calculate the total cost of the purchase
    total_cost = total_gum_cost + total_candy_cost
    result = total_cost
    return result

print(solution())