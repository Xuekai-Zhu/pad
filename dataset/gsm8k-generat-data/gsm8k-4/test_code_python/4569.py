def solution():
    """A rancher owns a mixture of 8 sheep and 5 cattle that graze on his land.  In a typical year, the rancher will allow his animals to feed off his pastures for as long as possible before they run out of grass.  After the pastures run out of grass, he must buy feed corn for $10 per bag.  Each cow eats 2 acres of grass per month, and each sheep eats 1 acre of grass per month.  Additionally, a bag of feed corn can feed each cow for 1 month and each sheep for 2 months.   If the rancher's pasture contains 144 acres of grass, how much will the rancher need to spend on feed corn to feed his animals each year?"""
    # Define the number of sheep and cattle
    num_sheep = 8
    num_cattle = 5

    # Define the amount of grass each sheep and cattle needs per month
    grass_per_month_sheep = 1
    grass_per_month_cattle = 2

    # Define the amount of time each sheep and cattle can be fed with one bag of feed corn
    feed_time_sheep = 2
    feed_time_cattle = 1

    # Define the cost of one bag of feed corn
    cost_per_bag = 10

    # Define the total amount of grass available
    total_grass = 144

    # Calculate the amount of grass needed per year
    grass_per_year = (num_sheep * grass_per_month_sheep + num_cattle * grass_per_month_cattle) * 12

    # Calculate the amount of feed corn needed per year
    feed_corn_needed = (grass_per_year - total_grass) / (num_sheep * feed_time_sheep + num_cattle * feed_time_cattle)

    # Calculate the total cost of feed corn
    cost_of_feed_corn = feed_corn_needed * cost_per_bag

    # return the result
    result = cost_of_feed_corn
    return result

print(solution())