def solution():
    num_chocolate_bars = 5
    chocolate_bar_price = 2

    total_paid = 20
    change = 4

    # Calculate the total cost of all chocolate bars
    total_chocolate_bar_cost = num_chocolate_bars * chocolate_bar_price

    # Calculate the cost of all items except chips
    total_without_chips = total_paid - change - total_chocolate_bar_cost

    # Calculate the cost per bag of chips
    cost_per_bag_of_chips = total_without_chips / 2
    result = cost_per_bag_of_chips
    return result

print(solution())