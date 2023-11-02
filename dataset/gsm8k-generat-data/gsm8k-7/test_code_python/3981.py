def solution():
    num_houses_day_1 = 20
    sell_rate_day_1 = 1  # sold in every house
    num_houses_day_2 = num_houses_day_1 * 2
    sell_rate_day_2 = 0.8  # sold in 80% of houses
    num_items_sold_day_1 = num_houses_day_1 * sell_rate_day_1 * 2 # sold two things in each house
    num_items_sold_day_2 = num_houses_day_2 * sell_rate_day_2 * 2 # sold two things in each house
    total_items_sold = num_items_sold_day_1 + num_items_sold_day_2
    result = total_items_sold
    return result

print(solution())