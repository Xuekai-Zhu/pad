def solution():
    """John has 25 horses. He feeds each horse twice a day and feeds them 20 pounds of food at each feeding. He buys half ton bags of food. How many of those will he have to buy in 60 days?"""
    num_horses = 25
    daily_food_per_horse = 20 * 2  # twice a day
    total_daily_food = num_horses * daily_food_per_horse
    num_days = 60
    total_food_needed = total_daily_food * num_days
    food_per_bag = 1000 / 2  # half-ton bag
    num_bags = total_food_needed / food_per_bag
    result = num_bags
    return result

print(solution())