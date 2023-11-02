def solution():
    # Calculate the total grass consumption of all animals in a year
    total_grass_consumption = (8 * 12 * 1) + (5 * 12 * 2)  # 8 sheep, each eat 1 acre per month for 12 months, and 5 cows, each eat 2 acres per month for 12 months

    # Calculate the number of months the animals can live without purchasing feed corn
    months_without_feed = 144 / total_grass_consumption  # assuming all animals consume grass at the same rate

    # Calculate the number of bags of feed corn needed to feed all animals for a year
    total_animals = 8 + 5
    bags_of_feed = (total_animals * 12 - months_without_feed * total_animals) / 2

    # Calculate the total cost of feed corn
    cost_of_feed = bags_of_feed * 10.0
    result = cost_of_feed
    return result

print(solution())