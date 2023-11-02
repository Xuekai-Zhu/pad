def solution():
    lollipop_cost = 1.5  # Each lollipop costs $1.50
    gummies_cost = 2  # Each pack of gummies costs $2
    num_lollipops = 4  # Chastity bought 4 lollipops
    num_gummies = 2  # Chastity bought 2 packs of gummies
    total_cost = (lollipop_cost * num_lollipops) + (gummies_cost * num_gummies)  # Calculate the total cost
    remaining_money = 15 - total_cost  # Calculate how much money Chastity has left
    result = remaining_money
    return result

print(solution())