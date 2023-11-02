def solution():
    num_candy_bars = 3
    candy_bar_cost = 25
    num_chocolates = 2
    chocolate_cost = 75
    num_juice_packs = 1
    juice_pack_cost = 50

    # Calculate the total cost of all the items
    total_cost = (num_candy_bars * candy_bar_cost) + (num_chocolates * chocolate_cost) + (num_juice_packs * juice_pack_cost)

    # Calculate the total number of quarters needed to buy all the items
    num_quarters = total_cost / 25
    result = num_quarters
    return result

print(solution())