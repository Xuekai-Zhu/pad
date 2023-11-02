def solution():
    # Calculate the total number of acres used by the animals per month
    total_acres_per_month = 5 * 2 + 8 * 1
    # Calculate the number of months the pasture will last
    months_of_grazing = 144 / total_acres_per_month
    # Calculate the number of cows and sheep that need to be fed after the pasture runs out
    cows_to_feed = 5 * months_of_grazing
    sheep_to_feed = 8 * months_of_grazing * 2
    # Calculate the total number of bags of feed corn needed
    total_bags_of_feed = cows_to_feed + sheep_to_feed / 2
    # Calculate the total cost of the feed corn
    total_cost = total_bags_of_feed * 10
    result = total_cost
    return result

print(solution())