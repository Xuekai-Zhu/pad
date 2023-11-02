def solution():
    num_sheep = 8  # The rancher owns 8 sheep
    num_cattle = 5  # The rancher owns 5 cattle
    pasture_size = 144  # The pasture is 144 acres in size
    cow_grass_use = 2  # Each cow eats 2 acres of grass per month
    sheep_grass_use = 1  # Each sheep eats 1 acre of grass per month
    feed_cost = 10  # A bag of feed corn costs $10
    cow_feed_duration = 1  # A bag of feed corn can feed a cow for 1 month
    sheep_feed_duration = 2  # A bag of feed corn can feed a sheep for 2 months

    # Calculate the total grass used each month by the cows and sheep
    total_grass_use = (num_cattle * cow_grass_use) + (num_sheep * sheep_grass_use)

    # Calculate the number of months the cows and sheep can feed on the pasture before running out of grass
    months_on_pasture = pasture_size / total_grass_use

    # Calculate the number of bags of feed corn needed for the cows and sheep after the pasture runs out of grass
    cow_feed_bags = num_cattle * (12 - months_on_pasture) * cow_feed_duration
    sheep_feed_bags = num_sheep * (24 - (2 * months_on_pasture)) * sheep_feed_duration

    # Calculate the total cost of feed corn needed for the cows and sheep
    total_feed_cost = (cow_feed_bags + sheep_feed_bags) * feed_cost
    result = total_feed_cost
    return result

print(solution())