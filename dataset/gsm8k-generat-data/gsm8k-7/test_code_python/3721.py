def solution():
    num_chocolate_bars = 10
    num_gummy_bears_packs = 10
    gummy_bears_pack_price = 2
    num_chocolate_chips_bags = 20
    chocolate_chips_bag_price = 5
    total_cost = 150

    # Calculate the total cost of all items except chocolate bars
    total_cost_without_chocolate_bars = (num_gummy_bears_packs * gummy_bears_pack_price) \
        + (num_chocolate_chips_bags * chocolate_chips_bag_price)

    # Calculate the cost of chocolate bars
    chocolate_bar_cost = total_cost - total_cost_without_chocolate_bars

    # Calculate the cost of one chocolate bar
    cost_of_one_chocolate_bar = chocolate_bar_cost / num_chocolate_bars
    result = cost_of_one_chocolate_bar
    return result

print(solution())