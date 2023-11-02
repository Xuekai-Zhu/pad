def solution():
    """A rancher owns a mixture of 8 sheep and 5 cattle that graze on his land. In a typical year, the rancher will allow his animals to feed off his pastures for as long as possible before they run out of grass. After the pastures run out of grass, he must buy feed corn for $10 per bag. Each cow eats 2 acres of grass per month, and each sheep eats 1 acre of grass per month. Additionally, a bag of feed corn can feed each cow for 1 month and each sheep for 2 months. If the rancher's pasture contains 144 acres of grass, how much will the rancher need to spend on feed corn to feed his animals each year?"""
    acres_of_grass = 144
    cows = 5
    sheep = 8
    cow_feed_time = 1
    sheep_feed_time = 2
    cow_feed_bags_needed = cows * 2 * cow_feed_time / 30
    sheep_feed_bags_needed = sheep * 1 * sheep_feed_time / 30
    total_feed_bags_needed = cow_feed_bags_needed + sheep_feed_bags_needed
    feed_cost_per_bag = 10
    total_feed_cost = total_feed_bags_needed * feed_cost_per_bag
    result = total_feed_cost
    return result

print(solution())