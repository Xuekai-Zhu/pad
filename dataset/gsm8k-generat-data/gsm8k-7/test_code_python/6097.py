def solution():
    num_horses = 25
    feed_per_horse = 20 # in pounds
    num_feedings_per_day = 2
    days = 60
    feed_per_bag = 1000 # in pounds

    # Calculate the total amount of food needed
    total_food = num_horses * feed_per_horse * num_feedings_per_day * days

    # Calculate the total number of bags needed
    total_bags = total_food / feed_per_bag

    result = total_bags / 0.5 # assuming each bag is half a ton
    return result

print(solution())