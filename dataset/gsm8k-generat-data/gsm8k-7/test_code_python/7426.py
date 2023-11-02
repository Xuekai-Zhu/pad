def solution():
    total_apples = 405
    juice = 90
    restaurant = 60
    sold = total_apples - juice - restaurant
    revenue = 408
    num_bags = sold / 5
    price_per_bag = revenue / num_bags
    result = price_per_bag
    return result

print(solution())